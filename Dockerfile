FROM python:3.9

ENV PYTHONUNBUFFERED=1

COPY ./app /app

COPY .env .env

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]