FROM python:3.8-alpine

RUN apk add --update postgresql-dev gcc python3-dev musl-dev py3-pip
RUN mkdir /app
WORKDIR /app

COPY ./api/requirements/ /app/requirements
RUN pip3 install -r /app/requirements/base.txt

COPY ./api/ /app

ENV FLASK_APP=main_app.py
ENV FLASK_ENV=development

CMD flask rq worker --verbose