from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length = 200)
    tipo = models.CharField(max_length = 50)
    is_owned = models.BooleanField(default = True)

