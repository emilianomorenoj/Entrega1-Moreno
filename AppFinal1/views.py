from urllib import request
from django.shortcuts import render
from AppFinal1.forms import *
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


def bikesinfoForm(request):

    if request.method == "POST":

        form2 = BikesInfoForm(request.POST)

        if form2.is_valid():
            
            info = form2.cleaned_data

            name2 = Bikeinfo(biketype=info["Bike Type"], wheelsize=info["Wheelsize"])

            name2.save()

            return render(request, "AppFinal1/home.html")

    else:

        form2 = BikesInfoForm()        

    return render(request, "AppFinal1/bikesinfoForm.html", {"form2": form2})




def racingeventForm(request):

    if request.method == "POST":

        form3 = RacingEventForm(request.POST)

        if form3.is_valid():
            
            info = form3.cleaned_data

            name3 = RacingEvent(racingevent=info["Race Type"], racelevel=info["Race Level"])

            name3.save()

            return render(request, "AppFinal1/home.html")

    else:

        form3 = RacingEventForm()        

    return render(request, "AppFinal1/racingeventForm.html", {"form3": form3})






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
