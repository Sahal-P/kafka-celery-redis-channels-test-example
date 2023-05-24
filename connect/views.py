from django.shortcuts import render, HttpResponse
from core.celery import add
from .kafka_consumer import consume_messages
from .kafka_producer import produce_message


def home(request):
    a = add.delay(1,2)
    return HttpResponse(f'hii{a}')

def produce(request):
    topic = 'my-topic'
    message = 'Hello, Kafka!'
    produce_message(topic, message)

    return HttpResponse('hi')
str = ''
