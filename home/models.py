from django.db import models

from tickets.models import Actor

class ActorImage(models.Model):
    actor = models.ForeignKey(Actor,
    null=False, blank=False, on_delete=models.CASCADE)
