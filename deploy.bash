supervisorctl reread
supervisorctl update
supervisorctl restart django_default

/usr/bin/python3 /projects/django_default/manage.py makemigrations
/usr/bin/python3 /projects/django_default/manage.py migrate
