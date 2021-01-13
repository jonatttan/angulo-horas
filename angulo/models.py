from django.db import models
from django.utils import timezone

class Angulo(models.Model):
    hour = models.IntegerField()
    minute = models.IntegerField()
    angle = models.IntegerField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = ("Angulo")
        verbose_name_plural = ("Angulos")

    def __str__(self):
        return self.hour#angle