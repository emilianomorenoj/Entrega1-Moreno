from socket import fromshare
from django import forms

class RidersInfoForm(forms.Form):

    name = forms.CharField(max_length=60)
    dateofbirth = forms.DateField()
    email = forms.EmailField()

