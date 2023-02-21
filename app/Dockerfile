FROM python:3.11 as dependencies

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements

# app stage
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim as app

RUN apt-get update && \
    apt-get -y install sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=dependencies /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
