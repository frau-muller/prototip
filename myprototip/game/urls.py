from django.urls import path

from .views import *
urlpatterns = [
    path('', indexx),
    path('test/', test),
]