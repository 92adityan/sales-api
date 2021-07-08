from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()

class Sale(models.Model):
    pass
