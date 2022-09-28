from django.urls import path
from AppFinal1.views import *

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
]