FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY . .

RUN pip install -r requirements.txt
