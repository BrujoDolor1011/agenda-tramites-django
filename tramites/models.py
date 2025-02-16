from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tramite(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('seguimiento', 'En seguimiento'),
        ('completo', 'Completo'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


