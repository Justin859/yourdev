from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

from .forms import ClientQuery, ClientForm

def index(request):
    return render(request, 'index.html')

def services(request):

    return render(request, 'services.html')

def get_started(request):

    if request.method == 'POST':
        form = ClientForm(request.PSOT)

        #if form.is_valid():
            # get cleanded data

    else:
        form = ClientForm()
    return render(request, 'get_started.html', {'form': form})

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

            messages.success(request, 'Your query has been sent.')
            return HttpResponseRedirect('/') 
    else:
        form = ClientQuery()
    return render(request, 'contact.html', {'form': form})