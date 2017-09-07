from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ClientQuery(forms.Form):
    
    client_name = forms.CharField(label='Your name', max_length=100, required=True)
    client_email = forms.EmailField(label='Your Email', max_length=255, required=True)
    client_query = forms.CharField(label='Your Query', max_length=1001, required=True)

class ClientForm(forms.Form):

    client_first_name = forms.CharField(label='first name', max_length=100, required=True, help_text='Enter your first name')
    client_last_name = forms.CharField(label='last name', max_length=100, required=True, help_text='Enter your last name')
    client_email = forms.EmailField(label='email', max_length=255, required=True, help_text='Enter a valid email address')
    
    company_name = forms.CharField(label='company name', max_length=255, required=True, help_text='Enter your company name')
    company_physical_address = forms.CharField(label='company address', max_length=1001, required=True, help_text="Enter your company's physical address")
    company_description = forms.CharField(label='company description', max_length=1001, required=True, help_text="Give a description of your company's products or services.")

    WEBSITE_TYPE = (('Web Application', 'Web Application'), ('Standard Website' ,'Standard Website'))

    has_domain = forms.BooleanField(label='does your company have a registered domain?', required=False)
    website_type = forms.ChoiceField(label='What type of website is needed?', choices=WEBSITE_TYPE, required=True)
    website_description = forms.CharField(label='website description', max_length=1001, required=True, help_text="Give a description of what your company would like the website to do.")

# Custom Validators

