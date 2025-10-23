# Deploying to Render (free plan)

This project provides a small helper script `start.sh` that runs database
migrations and `collectstatic` before starting Gunicorn. This is useful on the
Render free plan where the Dashboard's Pre-deploy/Release command is not
available.

Steps

1. In Render Dashboard create a new **Web Service** or edit your existing one.
2. In **Settings** → **Start Command** set:

```
./start.sh
```

3. Set environment variables for the service (Environment tab):

- `DATABASE_URL` — your PostgreSQL connection string (Render Managed DB)
- `DJANGO_SECRET_KEY` — set a secret key
- `DJANGO_DEBUG` — `false` in production
- `DJANGO_ALLOWED_HOSTS` — e.g. `your-service.onrender.com`
- `MIGRATE_ON_START` — optional; set to `false` to skip migrations/collectstatic on startup

4. Trigger a manual deploy or push to the `master` branch. The `start.sh` will
   run migrations and collectstatic, then start Gunicorn.

Notes

- `start.sh` is idempotent for migrations/collectstatic; ensure your code &
  migrations are in the repo before deploying.
- If you prefer infra-as-code, `render.yaml` is included and sets `startCommand` to `./start.sh`.
