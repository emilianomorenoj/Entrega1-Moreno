from urllib import request
from django.shortcuts import render
from AppFinal1.forms import RidersInfoForm
from AppFinal1.models import *
from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request,"AppFinal1/home.html")

def ridersinfo(request):
    
    return render(request,"AppFinal1/ridersinfo.html")

def bikesinfo(request):
    
    return render(request,"AppFinal1/bikesinfo.html") 

def racingevent(request):
    
    return render(request,"AppFinal1/racingevent.html")     

def ridersinfoForm(request):

    if request.method == "POST":

        form1 = RidersInfoForm(request.POST)

        if form1.is_valid():
            
            info = form1.cleaned_data

            name = RiderInfo(name=info["name"], dateofbirth=info["dateofbirth"], email=info["email"])

            name.save()

            return render(request, "AppFinal1/home.html")

    else:

        form1 = RidersInfoForm()        

    return render(request, "AppFinal1/ridersinfoForm.html", {"form1": form1})    



def searchEvent(request):

    return render(request, "AppFinal1/searchEvent.html")


def results(request):

    if request.GET["racingevent"]:

        racingevent = request.GET["racingevent"]
        racelevel = RacingEvent.objects.filter(racingevent__icontains=racingevent)

        return render(request, "AppFinal1/results.html", {"racingevent":racingevent, "racelevel":racelevel})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta) 
