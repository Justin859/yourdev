from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def services(request):

    return render(request, 'services.html')

def get_started(request):

    return render(request, 'get_started.html')

def contact(request):

    return render(request, 'contact.html')