from django.db import models


class Product(models.Model):
    title = models.TextField(max_length=20)
    description = models.TextField(max_length=120)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
