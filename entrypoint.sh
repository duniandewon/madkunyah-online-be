#!/bin/bash
set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

echo "Running database migrations..."
/app/.venv/bin/alembic upgrade head

echo "Starting FastAPI application on $HOST:$PORT..."
exec /app/.venv/bin/uvicorn app.app:app --host $HOST --port $PORT --workers 4