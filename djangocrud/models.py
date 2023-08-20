from django.db import models
# Create your models here.

from django.contrib.auth.models import User


class Discusion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    participantes = models.ManyToManyField(User, related_name='discusiones_participantes')
    
    def __str__(self):
        return self.titulo
    # Otros campos relevantes para la discusión

class Comentario(models.Model):
    discusion = models.ForeignKey(Discusion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()