from django.db import models

# Create your models here.


class Position(models.Model):
    id_key = models.IntegerField('Identification Key', primary_key=True)
    pos_name = models.CharField(max_length=100)
    pos_desc = models.CharField(max_length=1000)
    price_min = models.IntegerField()
    price_growth = models.IntegerField()
    price_start = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    state = models.CharField(max_length=100, default='used')
    pictures = models.CharField(max_length=100, default='prototyp')

