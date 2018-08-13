# Ewebsite from the junior company Emakers

## Technologies utilized
* Django 2.1
* Python 3.5.3
* Postgres 9.6.4

## Installation

Any Operating System:

```sh
virtualenv -p /usr/bin/python3 timesheet-env

source timesheet-env/bin/activate

pip install -r requeriments.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

access http://localhost:8000
```