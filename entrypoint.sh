#!/bin/bash
set -e

echo "Running database migrations..."
/app/.venv/bin/alembic upgrade head

echo "Starting FastAPI application..."
exec /app/.venv/bin/uvicorn app.app:app --host 0.0.0.0 --port 80 --workers 4