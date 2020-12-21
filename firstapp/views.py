from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def index(request):
    return HttpResponse("Hello Rajendra!")

def date(request):
    dt = datetime.datetime.now()
    s = '<b>Current Data Time </b>'+str(dt)
    return HttpResponse(s)