from wsgiref.util import request_uri
from django.shortcuts import render

def welcome(request):
    return render(request, 'account/welcome.html')
def login(request):
    return render(request, 'account/login.html')
def register(request):
    return render(request, 'account/register.html')