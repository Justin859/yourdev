from django import forms

class ClientQuery(forms.Form):
    
    client_name = forms.CharField(label='Your name', max_length=100)
    client_email = forms.EmailField(label='Your Email', max_length=255)
    client_query = forms.CharField(label='Your Query', max_length=1001)
