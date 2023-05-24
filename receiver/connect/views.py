from django.shortcuts import HttpResponse
from .kafka_consumer import consume_messages


def consume(request):
    topic = 'my-topic'
    consume_messages(topic)
    return HttpResponse(f'hic ')