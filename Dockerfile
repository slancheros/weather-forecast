FROM python:3-alpine

MAINTAINER Sandra Lancheros

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "weather-service.py"]