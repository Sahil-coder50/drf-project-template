#!/bin/sh
set -e

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL started"

if [ "$RUN_MIGRATIONS" = "1" ]; then
  echo "Running migrations..."
  python manage.py migrate --noinput
  python manage.py collectstatic --noinput
fi

exec "$@"