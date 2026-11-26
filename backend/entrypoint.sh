#!/bin/sh
# Ponto de entrada do container: aplica as migrações antes de iniciar o servidor.
set -e

python manage.py migrate --noinput

exec "$@"
