release: python3 ./scheduler-project/manage.py migrate
web: gunicorn scheduler-be/scheduler_project.wsgi --log-file -
