from urllib import request
from django.shortcuts import render
from AppFinal1.forms import *
from AppFinal1.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user: 
                
                login(request, user)

                return render(request, "AppFinal1/home.html", {"mensaje":f"Bienvenidx {user} a TransnavajasMTB 2022"})

        else:

            return render(request, "AppFinal1/home.html", {"mensaje":f"Datos incorrectos :( "})

    else:

        form = AuthenticationForm()

    return render(request, "AppFinal1/login.html", {"form": form})



def registro(request):

    if request.method == "POST":

        form = UserRegister(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppFinal1/home.html", {"mensaje": "Usuario creado con éxito"})

    else:

            form = UserRegister()

    return render(request, "AppFinal1/registro.html", {"form": form})

@login_required
def editarUser(request):

    usuario = request.user

    if request.method == "POST":
            
        form = FormEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppFinal1/home.html")
    else:

        form = FormEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name
        })

    return render(request, "AppFinal1/editarPerfil.html", {"formulario":form,"usuario":usuario})       







def home(request):

    return render(request,"AppFinal1/home.html")

def about(request):

    return render(request,"AppFinal1/about.html")

def ridersinfo(request):
    
    return render(request,"AppFinal1/ridsinfo.html")

def bikesinfo(request):
    
    return render(request,"AppFinal1/bikesinfo.html") 

def racingevent(request):
    
    return render(request,"AppFinal1/racingevent.html")     

@login_required
def ridersinfoForm(request): #crear riders info parte del CRUD

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




def racingeventForm(request): #crear race info parte del CRUD

    if request.method == "POST":

        form3 = RacingEventForm(request.POST, request.FILES)

        if form3.is_valid():
            
            info = form3.cleaned_data

            name3 = RacingEvent(racingevent=info["racingevent"], racelevel=info["racelevel"], imagen=info["imagen"])

            name3.save()

            return render(request, "AppFinal1/home.html")

    else:

        form3 = RacingEventForm()        

    return render(request, "AppFinal1/racingeventForm.html", {"form3": form3})


@login_required
def leerRacesInfo(request): # leer races info parte del CRUD

    races = RacingEvent.objects.all()

    return render(request, "AppFinal1/leerRacesInfo.html", {'races': races})




def searchEvent(request):
    if request.GET["racingevent"]:

        name = request.GET["racingevent"]
        events = RacingEvent.objects.filter(name__icontains=name)

        return render(request, "AppFinal1/results.html", {"events":events, "name": name})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def results(request):

    if request.GET["racingevent"]:

        racingevent = request.GET["racingevent"]
        racelevel = RacingEvent.objects.filter(racingevent__icontains=racingevent)

        return render(request, "AppFinal1/results.html", {"racingevent":racingevent, "racelevel":racelevel})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta) 


@login_required
def leerRidersInfo(request): # leer riders info parte del CRUD

    riders = RiderInfo.objects.all()

    contexto = {"Riders": riders}

    return render(request, "AppFinal1/leerRidersInfo.html", contexto)


@login_required
def eliminarRidersInfo(request, riderNombre):  # eliminar riders info parte del CRUD

    rider = RiderInfo.objects.get(name=riderNombre)
    rider.delete()


    riders = RiderInfo.objects.all()

    contexto = {"Riders": riders}

    return render(request, "AppFinal1/leerRidersInfo.html", contexto)


@login_required
def editarRidersInfo(request, riderNombre): #editar riders info parte del CRUD

    rider = RiderInfo.objects.get(name=riderNombre)

    if request.method == "POST":

        form1 = RidersInfoForm(request.POST)

        if form1.is_valid():
            
            info = form1.cleaned_data

            rider.name = info["name"]
            rider.dateofbirth = info["dateofbirth"]
            rider.email = info["email"]

            rider.save()

            return render(request, "AppFinal1/home.html")

    else:

        form1 = RidersInfoForm(initial={"Nombre":rider.name, "Fecha de nacimiento":rider.dateofbirth, 
        "Email":rider.email})        

    return render(request, "AppFinal1/editarRidersInfo.html", {"form1":form1, "Nombre": riderNombre})



def searchRiders(request):

    return render(request, "AppFinal1/home.html")


def resultsRiders(request):

    if request.GET["name"]:

        name = request.GET["name"]
        riders = RiderInfo.objects.filter(name__icontains=name)

        return render(request, "AppFinal1/home.html", {"riders": riders, "name": name})

    else: 

        answer = "No buscaste nada :( "


    return HttpResponse(answer)







