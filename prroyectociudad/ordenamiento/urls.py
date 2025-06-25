from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("parroquias/", views.lista_parroquias, name="lista_parroquias"),
    path("parroquias/nueva/", views.nueva_parroquia, name="nueva_parroquia"),
    path("barrios/", views.lista_barrios, name="lista_barrios"),
    path("barrios/nuevo/", views.nuevo_barrio, name="nuevo_barrio"),
]
