web: gunicorn config.wsgi
worker: celery -A config worker -B --loglevel=info