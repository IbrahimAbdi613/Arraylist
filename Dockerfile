FROM python:alpine

WORKDIR /app

COPY ./ArrayList.py .

CMD ["python3", "./ArrayList.py"]