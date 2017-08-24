from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

from .forms import ClientQuery

def index(request):
    return render(request, 'index.html')

def services(request):

    return render(request, 'services.html')

def get_started(request):

    return render(request, 'get_started.html')

def contact(request):

    if request.method == 'POST':
        form = ClientQuery(request.POST)

        if form.is_valid():
            name = form.cleaned_data['client_name']
            email = form.cleaned_data['client_email']
            query = form.cleaned_data['client_query']

            try:
                send_mail('yourdev.co.za Client Query', 'email: ' + email + '\n\nclient name: ' + name + '\n\nclient query: \n\n' + query, 'query@yourdev.co.za', ['info@yourdev.co.za'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')

            messages.success(request, 'Thank you for your query! We will contact you as soon as possible.')
            return HttpResponseRedirect('/') 

    return render(request, 'contact.html')