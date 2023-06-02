from django.shortcuts import HttpResponse
from .kafka_consumer import consume_messages


def consume(request):
    
    return HttpResponse('hii')