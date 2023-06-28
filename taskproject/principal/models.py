from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(default=datetime.now, blank=True)
    STATUS_CHOICES = (
        ('P', 'Pendiente'),
        ('IP', 'En progreso'),
        ('C', 'Completada'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    LABEL_CHOICES = (
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baja'),
    )
    label = models.CharField(max_length=2, choices=LABEL_CHOICES)

# Opciones para el campo etiqueta
# Al momento de el usuario crear la tarea se le debe poder asignar una etiqueta, la cual puede ser una de las siguientes:
# Pagado (P) - La tarea se ha pagado
# No pagado (NP) - La tarea no se ha pagado
# Envío (E) - La tarea se ha enviado
