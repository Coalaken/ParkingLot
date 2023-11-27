.PHONY: install
install:
	poetry install


.PHONY: run
run:
	poetry run python3.10 -m core.manage runserver 0.0.0.0:8000


.PHONY: migrate
migrate:
	poetry run python3.10 -m core.manage migrate


.PHONY: migrations
migrations:
	poetry run python3.10 -m core.manage makemigrations


.PHONY: createsuperuser
createsuperuser:
	poetry run python3.10 -m core.manage createsuperuser