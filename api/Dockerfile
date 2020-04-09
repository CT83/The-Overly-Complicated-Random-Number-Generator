FROM python:3.8-alpine

RUN apk add --update postgresql-dev gcc python3-dev musl-dev py3-pip

RUN mkdir /app
WORKDIR /app

COPY requirements/base.txt /app/requirements/base.txt
RUN pip3 install -r /app/requirements/base.txt

COPY . /app

RUN chmod +x start_flask.sh

ENV FLASK_APP=main_app.py
ENV FLASK_ENV=development

CMD ["./start_flask.sh"]