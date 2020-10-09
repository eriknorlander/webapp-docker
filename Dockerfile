FROM python:3.6-alpine

WORKDIR /app

RUN pip install flask

COPY app.py .

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

