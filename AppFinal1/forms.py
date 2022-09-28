from socket import fromshare
from django import forms

class RidersInfoForm(forms.Form):

    name = forms.CharField(max_length=60)
    dateofbirth = forms.DateField()
    email = forms.EmailField()

class BikesInfoForm(forms.Form):

    biketype = forms.CharField(max_length=60)
    wheelsize = forms.CharField(max_length=60)



class RacingEventForm(forms.Form):

    racingevent = forms.CharField(max_length=60)
    racelevel = forms.CharField(max_length=60)
