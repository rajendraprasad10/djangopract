from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def quote(request):
    return HttpResponse("This ia from quote response")