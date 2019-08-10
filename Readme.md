# Portfolio

Portfolio of SDSLabs made in Django and Vue.

## Setup Instructions

- Install python and pip.
- Install virtualenv.
- Clone the github repository.
- Go the root directory of the project and run `virtualenv -p python3 ./venv`.
- Activate the virtualenv with `source ./venv/bin/activate`.
- Run `pip install -r settings/requirements-common.txt`.
- Run `pip install -r settings/dev/requirements-dev.txt` or `pip install -r settings/prod/requirements-prod.txt` depending on the environment.

The next 2 steps are for installing postgresql. Alternatively, if you do not want to use docker you can install postgresql on your own.

- Make sure `docker` and `docker-compose` is installed.
- Run `docker-compose -f settings/dev/postgres-docker-compose.yml up -d`.

- Once you have an up and running configuration of postgresql copy `settings/dev/settings.sample.py` to `settings/dev/settings.py` and update the postgresql credentials.
- Run `python manage.py createsuperuser --settings=settings.dev.settings`.
- Run `python manage.py migrate --settings settings.dev.settings`.
- Run `python manage.py runserver --settings settings.dev.settings`.
- Open `localhost:8000/admin` to verify that your django backend is working perfectly.
- Go to the `frontend` directory.
- Run `npm install`.
- Run `npm run serve`.
- Open `localhost:8080` to see the frontend.
