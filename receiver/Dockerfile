FROM python:3
ENV PYTHONUNBUFFERED = 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install confluent-kafka
