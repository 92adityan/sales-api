from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name

class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    def getDate(self):
        return self.date.strftime('%B/%d/%Y')
