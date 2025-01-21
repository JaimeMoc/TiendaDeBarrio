# Comandos para el proyecto. Usamos "make NOMBREDELCOMANDO"
runserver:
	python manage.py runserver --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

test:
	python manage.py test --settings=settings.local

test-one:
	python manage.py test $(TEST_NAME) --settings=settings.local

shellplus:
	python manage.py shell_plus --ipython --settings=settings.local