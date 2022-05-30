python manage.py migrate --noinput
gunicorn --worker-tmp-dir /dev/shm core.wsgi
