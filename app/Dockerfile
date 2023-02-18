FROM python:3.11 as build

COPY requirements ./

RUN pip install --user --no-cache-dir -r requirements

# app stage
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim as app

COPY --from=build /root/.local /root/.local

RUN apt-get update && \
    apt-get -y install sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH=/root/.local/bin:$PATH

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
