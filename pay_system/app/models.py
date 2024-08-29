from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    price = models.DecimalField(max_digits=8, decimal_places=2)

