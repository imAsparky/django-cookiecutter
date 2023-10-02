#!/bin/bash
set -e

# Get the correct Database URL.
{% if cookiecutter.deploy_with_docker != "swarm" %}
if [ -n "$LOCAL_DATABASE_URL" ]; then
    CHECK_DATABASE_URL=$LOCAL_DATABASE_URL
    DB_ENVIRONMENT="LOCAL DATABASE"
elif [ -n "$TESTING_DATABASE_URL" ]; then
    CHECK_DATABASE_URL=$TESTING_DATABASE_URL
    DB_ENVIRONMENT="TESTING DATABASE"
elif [ -n "$STAGING_DATABASE_URL" ]; then
    CHECK_DATABASE_URL=$STAGING_DATABASE_URL
    DB_ENVIRONMENT="STAGING DATABASE"
elif [ -n "$PROD_DATABASE_URL" ]; then
    CHECK_DATABASE_URL=$PROD_DATABASE_URL
    DB_ENVIRONMENT="PRODUCTION DATABASE"
elif [ -n "$DATABASE_URL" ]; then
    CHECK_DATABASE_URL=$DATABASE_URL
    DB_ENVIRONMENT="DB ENV NOT SUPPLIED. USING DEFAULT URL"

fi

if [ -n "$CHECK_DATABASE_URL" ]; then
    >&2 echo "OH NICE.....THERE IS A DATABASE URL HERE MATE"
    # Check to see if the Database is available.
    until psql "$CHECK_DATABASE_URL" -c '\l'; do
    >&2 echo "Checking Postgres availability."$'\n'"DB ENVIRONMENT: {$DB_ENVIRONMENT}"$'\n'"Postgres DB is unavailable - sleeping 10!"
    sleep 10
    done
else

    >&2 echo "DUOH.....THERE IS NO DATABASE URL HERE MATE!"$'\n'"EXITING!!!"
    exit 1

fi

>&2 echo "Postgres is up - continuing"
{% endif %}
if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    >&2 echo "Postgres is up - Attempting to migrate."
    python manage.py migrate --noinput
fi

exec "$@"
