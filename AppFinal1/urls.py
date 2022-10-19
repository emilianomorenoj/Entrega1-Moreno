from django.urls import path
from AppFinal1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("home/", home, name="Home"),
    path("ridersinfo/", ridersinfo, name="Riders"),
    path("bikesinfo/", bikesinfo, name="Biclas"),
    path("racingevent/", racingevent, name="Races"),
    path("ridersinfoForm/", ridersinfoForm, name="RidersinfoForm"),
    path("bikesinfoForm/", bikesinfoForm, name="BikesinfoForm"),
    path("racingeventForm/", racingeventForm, name="RacingeventForm"),
    path("searchEvent/", searchEvent, name="SearchEvent"), 
    path("results/", results, name="SearchResults"),
    path("login/", login_request, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout/", LogoutView.as_view(template_name="AppFinal1/logout.html"), name="Logout"),
    path("editarPerfil/", editarUser, name = "EditarUser"),
    path("resultsRider/", resultsRiders, name="ResultsRiders"), 
    path("searchRider/", searchRiders, name="SearchRiders"),
    path("about/", about, name="About"),
    




    #CRUD de Riders y Races
    path("leerRiders/", leerRidersInfo, name="LeerRidersInfo"),
    path("eliminarRiders/<riderNombre>/", eliminarRidersInfo, name="EliminarRider"),
    path("editarRiders/<riderNombre>/", editarRidersInfo, name="EditarRider"),
    path("leerRaces/", leerRacesInfo, name="LeerRacesInfo"),
]

