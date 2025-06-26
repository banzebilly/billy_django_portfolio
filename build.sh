#!usr/bin/env bash
#exit on error

set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser if environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
  python manage.py createsuperuser \
    --no-input \
    --email "$DJANGO_SUPERUSER_EMAIL"
fi




# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate

# if [[ $CREATE_SUPERUSER]];
# then
#    python mange.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL
# fi
#!/usr/bin/env bash
# Exit on error