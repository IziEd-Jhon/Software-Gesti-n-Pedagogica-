from django.db import models

class Activity(models.Model):
    title   = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural="Actividades"
