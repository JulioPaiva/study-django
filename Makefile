install-deps: 
	poetry install


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
