from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.produce),
    path('consume', views.consume),
]
