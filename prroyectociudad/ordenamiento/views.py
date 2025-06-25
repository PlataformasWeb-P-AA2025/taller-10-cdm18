from django.shortcuts import render, redirect, get_object_or_404
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm

# Vista de inicio
def inicio(request):
    return render(request, "ordenamiento/base.html")


# Lista de parroquias con sus barrios
def lista_parroquias(request):
    parroquias = Parroquia.objects.all()
    return render(request, "ordenamiento/lista_parroquias.html", {"parroquias": parroquias})


# Lista de barrios
def lista_barrios(request):
    barrios = Barrio.objects.select_related("parroquia").all()
    return render(request, "ordenamiento/lista_barrios.html", {"barrios": barrios})


# Crear nueva parroquia
def nueva_parroquia(request):
    if request.method == "POST":
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_parroquias")
    else:
        form = ParroquiaForm()

    return render(request, "ordenamiento/form_parroquias.html", {"form": form})


# Crear nuevo barrio
def nuevo_barrio(request):
    if request.method == "POST":
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_barrios")
    else:
        form = BarrioForm()

    return render(request, "ordenamiento/form_barrios.html", {"form": form})
