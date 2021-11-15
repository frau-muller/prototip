
from django.urls import path
from .views import *


urlpatterns = [
    path('',welcome),
    path('',login),
    path('' ,register),
    path('',logout),

]