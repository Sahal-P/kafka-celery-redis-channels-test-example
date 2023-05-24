from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('produce', views.produce),
    path('consume', views.consume),
]
