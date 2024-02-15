#!/bin/sh

if ["$DATABASE" = "postgres"]
then
    echo "Waiting for postgres"

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

poetry install
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createcachetable
poetry run python manage.py collectstatic --no-input --clear

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    poetry run python manage.py createsuperuser \
        --noinput 
fi

exec "$@"