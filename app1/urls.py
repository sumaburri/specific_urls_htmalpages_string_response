from django.urls import path
from app1.views import *
app_name='somthing'

urlpatterns = [
    path('red/',red,name='red'),
]