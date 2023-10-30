from django.db import models

# Create your models here.
class Tarea(models.Model):
    
    ESTADO_CHOICES = (
        ('pendiente','Pendiente'),
        ('terminado','Terminado')
    )
    
    descripcion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50,choices=ESTADO_CHOICES)