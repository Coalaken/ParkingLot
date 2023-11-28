FROM python:3.10


WORKDIR /app

COPY ./apps .
COPY ./core .
COPY ./locals .
COPY ./Makefile .
COPY ./pyproject.toml .

RUN pip install poetry

RUN poetry install

EXPOSE 8000