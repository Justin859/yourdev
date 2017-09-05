from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

from .forms import ClientQuery, ClientForm

# Global functions

def check_browser(browser, view):
    if browser == 'IE' or browser == 'Edge':
        return 'ms_templates/' + view
    else:
        return view
# Views

def index(request):
    page = check_browser(request.user_agent.browser.family, 'index.html')

    return render(request, page)

def services(request):

    page = check_browser(request.user_agent.browser.family, 'services.html')

    return render(request, page)

def get_started(request):

    page = check_browser(request.user_agent.browser.family, 'get_started.html')

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            client_first_name = form.cleaned_data['client_first_name']
            client_last_name = form.cleaned_data['client_last_name']
            client_email = form.cleaned_data['client_email']

            company_name = form.cleaned_data['company_name']
            company_physical_address = form.cleaned_data['company_physical_address']
            company_description = form.cleaned_data['company_description']

            has_domain = form.cleaned_data['has_domain']
            website_type = form.cleaned_data['website_type']
            website_description = form.cleaned_data['website_description']

            try:
                send_mail('yourdev.co.za Client Submission',
                '\n\nCLIENT DETAILS\n' + '----------------------' +
                 '\n\nClient Email:  ' + client_email +
                 '\n\nClient Name:  ' + client_first_name + ' ' + client_last_name +
                  '\n\nCOMPANY DETAILS\n' + '----------------------' +
                   '\n\nCompany Name:  ' + company_name +
                   '\n\nPHYSICAL ADDRESS:\n\n' + company_physical_address +
                   '\n\nCOMPANY DESCRIPTION:\n\n' + company_description +
                    '\n\nRegistered Domain:  ' + str(has_domain) +
                    '\n\nType of Website:  ' + website_type +
                    '\n\nWEBSITE DESCRIPTION:\n\n' + website_description,
                    'query@yourdev.co.za', ['info@yourdev.co.za'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')

            messages.success(request, 'Thank you for your submission. Your form has been submitted. You will recieve a Quote/ Proposal within 48hrs.')
            return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return render(request, page, {'form': form})

def contact(request):

    page = check_browser(request.user_agent.browser.family, 'contact.html')

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

            messages.success(request, 'Thank you for your query! Your query has been sent. We will contact you as soon as possible.')
            return HttpResponseRedirect('/') 
    else:
        form = ClientQuery()
    return render(request, page, {'form': form})