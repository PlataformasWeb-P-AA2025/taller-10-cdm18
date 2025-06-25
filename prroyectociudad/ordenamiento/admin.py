from django.contrib import admin
from .models import Parroquia, Barrio

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "tipo")
    list_filter = ("ubicacion", "tipo")
    search_fields = ("nombre",)

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "parroquia",
        "numero_viviendas",
        "numero_parques",
        "numero_edificios_residenciales",
    )
    list_filter = ("parroquia", "numero_parques")
    search_fields = ("nombre",)
