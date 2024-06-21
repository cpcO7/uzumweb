migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

loaddata:
    python3 manage.py loaddata region district