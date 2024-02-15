FROM python:3-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y netcat

RUN pip3 install poetry

COPY ./entrypoint.sh .
RUN chmod +x /home/app/web/entrypoint.sh

COPY . $APP_HOME

#RUN chown -R app:app $APP_HOME

#USER app

ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]