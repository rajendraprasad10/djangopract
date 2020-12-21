from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def index(request):
    myname = {
        'name' : 'rajendra'
    }
    return render(request, 'index.html', myname)

def Employedetail(request):
    empdetails = {
        'id' : 123,
        'name': 'rajendra prasad',
        'salary': 20000
    }
    return render(request, 'employedetail.html', empdetails)