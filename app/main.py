import os
import random
import sqlite3
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_health import HealthCheck, HealthCheckResponse
from pydantic import BaseModel
from datetime import datetime
from cachetools import cached, TTLCache

app = FastAPI()
security = HTTPBearer()

class Word(BaseModel):
    word: str


db_path = os.environ.get('DB_PATH', 'api_calls.db')
max_calls = int(os.environ.get('MAX_CALLS', 100))
return_limit = int(os.environ.get('RETURN_LIMIT', 10))

auth_token = os.environ.get('AUTH_TOKEN', 'mysecretkey')

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials or not credentials.scheme == 'Bearer':
        raise HTTPException(status_code=401, detail='Invalid authentication credentials')
    if not credentials.credentials == auth_token:
        raise HTTPException(status_code=401, detail='Invalid token')
    return True

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_calls (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            input_word TEXT,
            random_word TEXT
        )
    ''')
    conn.commit()
    cursor.execute(f'''
        DELETE FROM api_calls WHERE id NOT IN (
            SELECT id FROM api_calls ORDER BY timestamp DESC LIMIT {max_calls}
        )
    ''')
    conn.commit()


def add_api_call(input_word, random_word):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO api_calls (timestamp, input_word, random_word)
            VALUES (?, ?, ?)
        ''', (timestamp, input_word, random_word))
        conn.commit()


# caches the results of get_api_calls for 10 seconds
@cached(cache=TTLCache(maxsize=128, ttl=10))
def get_api_calls(limit=return_limit):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT timestamp, input_word, random_word
            FROM api_calls
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        rows = cursor.fetchall()
        api_calls = []
        for row in rows:
            api_calls.append({
                "timestamp": row[0],
                "input_word": row[1],
                "random_word": row[2]
            })
        return {"api_calls": api_calls}

health = HealthCheck()

def simple_check():
    return True

health.add_check(simple_check)

# def check():
#     # Perform health checks here
#     status = "pass"
#     if not status:
#         return 503  # Service Unavailable
#     return 200  # OK

@app.post("/jumble")
def randomize_word(word: Word, authenticated: bool = Depends(authenticate)):
    input_word = word.word
    word_list = list(input_word)
    random.shuffle(word_list)
    random_word = ''.join(word_list)
    add_api_call(input_word, random_word)
    return {"random_word": random_word}


@app.get("/audit")
def api_calls(request: Request, authenticated: bool = Depends(authenticate)):
    limit = request.query_params.get('limit', return_limit)
    return get_api_calls(limit=limit)

@app.get("/health")
def health_check():
    response = HealthCheckResponse(health.check())
    return response.dict()
