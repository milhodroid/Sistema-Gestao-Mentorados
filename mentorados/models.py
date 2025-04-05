from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Navigator será uma pessoa que acompanhará o mentorado durante o programa
class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Mentorados(models.Model):
    estagio_choices = (
        ('E1', '10-100'),
        ('E2', '100-500'),
        ('E3', '500-1000')
    )
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    navigator = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome