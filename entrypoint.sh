#!/bin/ash
echo "Applying Database Migration"
python manage.py migrate
exec "$@"