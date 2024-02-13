FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry install