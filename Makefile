mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

load:
	python3 manage.py loaddata region district categories

user:
	python3 manage.py createsuperuser