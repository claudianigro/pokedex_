from django.db import models
import uuid

class Allenatore(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    surname = models.CharField(max_length = 50, unique = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)