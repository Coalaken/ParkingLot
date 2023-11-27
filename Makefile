.PHONY: install
install:
	poetry install


.PHONY: run
run:
	poetry run python3.10 -m core.manage runserver 0.0.0.0:8000