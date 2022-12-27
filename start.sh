#! /usr/bin/env sh
set -e

# Run migrations
alembic upgrade head

# Start backend
exec uvicorn app.main:app --reload --host 0.0.0.0 --port 80
