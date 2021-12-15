# Adapted from https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
# https://pythonspeed.com/articles/multi-stage-docker-python/ for smaller images

# Compile image
FROM python:3.9-slim-bullseye AS compile-image
# FROM python:3.9-slim-bullseye
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV_COMP=/venv_compile
RUN python3 -m venv $VIRTUAL_ENV_COMP
ENV PATH="$VIRTUAL_ENV_COMP/bin:$PATH"

# Copy requirements files
# Change the path to your production requirements file if different.
COPY config/requirements/ /config/requirements/

# Install build deps, run `pip install`, remove unneeded build deps.
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential=12.9 \
    libpcre3-dev=2:8.39-13 \
    libpq-dev=13.5-0+deb11u1 \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --upgrade pip\
    && pip install --no-cache-dir -r /config/requirements/production.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

###############################################################################

# Production image
FROM python:3.9-slim-bullseye AS production-image

ARG USER=django
RUN groupadd -r ${USER} && useradd --no-log-init -r -g ${USER} ${USER}
ENV VIRTUAL_ENV_PROD=/venv_prod
ENV PATH="$VIRTUAL_ENV_PROD/bin:$PATH"

# Install packages needed to run your application.
#   mime-support -- for mime types when serving static files
#   postgresql-client -- for running database commands
RUN set -ex \
    && RUN_DEPS=" \
    libpcre3=2:8.39-13 \
    mime-support=3.66 \
    postgresql-client=13+225 \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt-get/lists/* \
    && echo sed -i 's/\r$//g' /entrypoint

WORKDIR /home/${USER}

# # Copy all the Run Dependencies from the compile-image and set the owner to $USER
COPY --chown=${USER}:${USER} --from=compile-image venv_compile ${VIRTUAL_ENV_PROD}

WORKDIR /home/${USER}

# Add the minimum project files required for production
# To add all files from the project directory comment these out and see next comment.
COPY --chown=${USER}:${USER} django_boilerplate django_boilerplate
COPY --chown=${USER}:${USER} manage.py manage.py
COPY --chown=${USER}:${USER} config/settings/ config/settings/
COPY --chown=${USER}:${USER} templates templates
COPY --chown=${USER}:${USER} docker-entrypoint.sh docker-entrypoint.sh
# Uncomment this line copies all folders and files from your project directory.
# Copy --chown=${USER}:${USER} . .

# uWSGI will listen on this port
EXPOSE 8000

# Add any static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN DATABASE_URL='' python3 manage.py collectstatic --noinput

# Tell uWSGI where to find your wsgi file (change this):
ENV UWSGI_WSGI_FILE=django_boilerplate/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# uWSGI static file serving configuration (customize or comment out if not needed):
ENV UWSGI_STATIC_MAP="/static/=./static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

# Preferable do this with Traefik edge router.
# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8000$) break:400"

# Change to a non-root user
USER ${USER}:${USER}

ENTRYPOINT ["./docker-entrypoint.sh"]

# Start uWSGI
CMD ["uwsgi", "--show-config"]
