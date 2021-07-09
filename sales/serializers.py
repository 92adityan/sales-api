from rest_framework import serializers
from .models import Order


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'itemsTotal', 'saleTotal', 'date')