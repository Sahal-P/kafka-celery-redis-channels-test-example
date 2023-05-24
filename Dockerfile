FROM python:3
ENV PYTHONUNBUFFERED = 1
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y build-essential
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install confluent-kafka
