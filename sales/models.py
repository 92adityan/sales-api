from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True)
    date = models.DateField()
    order_id = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.order_id)
    
    def getDate(self):
        return self.date.strftime('%d/%m/%Y')

    @property
    def saleTotal(self):   
        items = self.orderitem_set.all()
        total = sum([item.totalAmount() for item in items])
        return total
        
    @property
    def itemsTotal(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField(default = 0)
    date_added = models.DateField()

    class Meta:
        ordering = ['-quantity']

    def __str__(self):
        return str(self.id)

    def totalAmount(self):
        return self.item.item_price *  self.quantity
    
    def item_quantity(self):
        return [self.item.item_name, self.quantity]