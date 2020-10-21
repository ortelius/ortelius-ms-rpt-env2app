FROM python:3.8-alpine
ENV PYTHONUNBUFFERED True
EXPOSE 5000
WORKDIR /app
ADD . /app

RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev postgresql-dev; \
    pip install -r requirements.txt
CMD ["waitress-serve","--port=5000", "msapi:app"]