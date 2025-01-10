FROM nginx:latest

COPY conf /etc/nginx/conf.d/default.conf
COPY /build /usr/share/nginx/html

ENV APP_HOME=/home/app/web
RUN mkdir -p ${APP_HOME}
RUN mkdir -p ${APP_HOME}/staticfiles