from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home page")


def login(request):
    dict = {'name': "Login"}
    return render(request, 'login.html', context=dict)


