.PHONY: install
install:
	poetry install


.PHONY: run
run:
	poetry run python3 autostate/manage.py runserver 0.0.0.0:8000