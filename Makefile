run:
	python manage.py runserver --settings=cts_pro.settings.common

push:
	git push cts "$r"