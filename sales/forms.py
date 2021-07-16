from django.db.models.base import Model
from django.forms import ModelForm
from .models import Order, OrderItem
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    date = forms.DateField(widget=DateInput)

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    date_added = forms.DateField(widget=DateInput)