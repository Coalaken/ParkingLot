FROM python:3.10


WORKDIR /app

COPY ./apps ./apps/
COPY ./core ./core/
COPY ./locals ./locals/
COPY ./req.txt .

RUN pip install -r req.txt
RUN python3 -m core.manage migrate

EXPOSE 8000