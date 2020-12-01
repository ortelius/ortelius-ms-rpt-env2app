FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11
WORKDIR /app
COPY . /app
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev postgresql-dev; \
    pip install -r requirements.txt; \
    pip install --upgrade meinheld
