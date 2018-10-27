from django.db import models

# Create your models here.
class client_info(models.Model):
    client_id = models.IntegerField()
    cpu_info=models.FloatField()
    objects = models.Manager()
