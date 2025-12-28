#!/bin/sh

su -m root -c "python manage.py migrate"

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Running in production mode"
    su -m root -c "python manage.py collectstatic --noinput"
    su -m root -c "gunicorn --workers=4 --worker-class=gevent --bind 0.0.0.0:8000 movie_rating_system.wsgi"
else
    echo "Running in development mode"
    su -m root -c "python manage.py runserver 0.0.0.0:8000"
fi