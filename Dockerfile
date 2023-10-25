FROM python:3.9.17-slim

WORKDIR /app

COPY . /app

RUN pip install tornado

CMD ["python", "app.py"]