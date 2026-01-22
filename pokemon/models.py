from django.db import models
import uuid
from allenatore.models import Allenatore

class Pokemon(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pokedex_id = models.IntegerField()
    allenatore = models.ForeignKey(Allenatore, on_delete = models.CASCADE, related_name = "pokemon", null = True, blank=True)


