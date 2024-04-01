from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def yellow(request):
    return HttpResponse('MANGO IS A YELLOW COLOUR')
