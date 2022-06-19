from django.db import models


class ButtonCount(models.Model):
    frequency = models.IntegerField()
    pressed = models.BooleanField(default=False)
