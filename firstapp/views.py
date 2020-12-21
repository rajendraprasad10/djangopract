from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def index(request):
    myname = {
        'name' : 'rajendra'
    }
    return render(request, 'index.html', myname)


def eletronics(request):
    ele_dic = {
        'product1' : 'iphone',
        'product2': 'mac',
        'product3': ',macbook',

    }
    return render(request, 'eletronics.html', ele_dic)


def toys(request):
    ele_dic = {
        'product1': 'drons',
        'product2': 'remote cars',
        'product3': 'robot cars',

    }
    return render(request, 'toys.html', ele_dic)


def shoes(request):
    ele_dic = {
        'product1': 'adidas',
        'product2': 'rebook',
        'product3': 'puma',

    }
    return render(request, 'shoes.html', ele_dic)


def Employedetail(request):
    empdetails = {
        'id' : 123,
        'name': 'rajendra prasad',
        'salary': 20000
    }
    return render(request, 'employedetail.html', empdetails)