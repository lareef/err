python manage.py migrate --noinput
gunicorn --worker-tmp-dir /dev/shm core.wsgi
python manage.py createsuperuser --noinput --user lareef --email lareef.lafir@gmail.com