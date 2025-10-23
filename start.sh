#!/usr/bin/env bash
# start.sh - runs optional migrations and collectstatic, then starts gunicorn
set -euo pipefail

echo "Starting startup script..."

# Default: run migrations and collectstatic on start. Set MIGRATE_ON_START=false to skip.
MIGRATE_ON_START="${MIGRATE_ON_START:-true}"

if [ "$MIGRATE_ON_START" = "true" ]; then
  echo "MIGRATE_ON_START is true — running database migrations"
  # Run migrations (non-interactive). Fail the boot if migrations fail.
  python manage.py migrate --noinput

  echo "Collecting static files"
  python manage.py collectstatic --noinput
else
  echo "MIGRATE_ON_START is false — skipping migrations and collectstatic"
fi

echo "Starting Gunicorn"
exec gunicorn vidly.wsgi:application --bind 0.0.0.0:$PORT
