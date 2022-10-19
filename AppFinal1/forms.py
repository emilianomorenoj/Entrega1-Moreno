from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppFinal1.models import RacingEvent

class RidersInfoForm(forms.Form):

    name = forms.CharField(max_length=60)
    dateofbirth = forms.DateField()
    email = forms.EmailField()

class BikesInfoForm(forms.Form):

    biketype = forms.CharField(max_length=60)
    wheelsize = forms.CharField(max_length=60)



class RacingEventForm(forms.ModelForm):

    class Meta:

        model = RacingEvent
        fields = ['racingevent', 'racelevel', 'imagen']



class UserRegister(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class FormEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]
