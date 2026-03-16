install-deps:
	poetry install

install-prod:
	poetry install --only main


run-app:
	poetry run python manage.py runserver


django-version:
	poetry run python -m django --version

django-poetry:
	poetry show django


start-project:
	poetry run python -m django-admin startproject manage .

start-project2:
	poetry run django-admin startproject manage .


start-app:
	poetry run django-admin startapp core


makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

create-superuser:
	poetry run python manage.py createsuperuser


lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check . --fix


tests:
	poetry run pytest

coverage:
	poetry run pytest --cov

coverage-core:
	poetry run pytest --cov=core --cov-report=term --cov-report=html

django-help:
	poetry run python manage.py help

django-shell:
	poetry run python manage.py shell
