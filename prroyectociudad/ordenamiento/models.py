from django.db import models

class Parroquia(models.Model):
    UBICACION_CHOICES = [
        ("N", "Norte"),
        ("S", "Sur"),
        ("E", "Este"),
        ("O", "Oeste"),
    ]
    TIPO_CHOICES = [("urbana", "Urbana"), ("rural", "Rural")]

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=1, choices=UBICACION_CHOICES)
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Barrio(models.Model):
    PARQUES_CHOICES = [(i, str(i)) for i in range(1, 7)]

    nombre = models.CharField(max_length=100)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.PositiveSmallIntegerField(choices=PARQUES_CHOICES)
    numero_edificios_residenciales = models.PositiveIntegerField()
    parroquia = models.ForeignKey(
        Parroquia, on_delete=models.CASCADE, related_name="barrios"
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} – {self.parroquia.nombre}"
