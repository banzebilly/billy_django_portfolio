

#!/usr/bin/env bash
# Exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate

# if [[ $CREATE_SUPERUSER ]]; then
#    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
# fi
#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER == "True" ]]; then
  echo "Checking if superuser exists..."
  python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "${DJANGO_SUPERUSER_USERNAME}"
email = "${DJANGO_SUPERUSER_EMAIL}"
password = "${DJANGO_SUPERUSER_PASSWORD}"
if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Superuser already exists, skipping creation.")
EOF
fi
