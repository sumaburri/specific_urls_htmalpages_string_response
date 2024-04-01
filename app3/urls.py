from django.urls import path
from app3.views import *
app_name='nothing'
urlpatterns = [
    path('yellow/',yellow,name='yellow'),
]