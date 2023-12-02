FROM python:3.10-alpine3.16


WORKDIR /app

COPY ./apps ./apps/
COPY ./core ./core/
COPY ./locals ./locals/
COPY ./req.txt .

RUN pip install --upgrade pip
RUN pip install -r req.txt

EXPOSE 8000