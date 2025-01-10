FROM python:3.12.8-alpine AS builder

# create folder for storing staticfiles
ENV APP_HOME=/home/app/web
RUN mkdir -p ${APP_HOME}
RUN mkdir -p ${APP_HOME}/staticfiles

WORKDIR /usr/app/django_oauth
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .

EXPOSE 8000