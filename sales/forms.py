from django.db.models.base import Model
from django.forms import ModelForm
from .models import Order, OrderItem


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' 


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'