from django.shortcuts import render
from .models import OrderItem, Order
import datetime
from rest_framework import viewsets
from .serializers import SaleSerializer
from .filters import SaleFilter

def dashboard_view(request):
    orders = Order.objects.all()
    orderitems = OrderItem.objects.all()

    item_dict = {}
    for orderitem in orderitems:
        item, quantity = orderitem.item_quantity()
        if item in item_dict:
            previous_quantity = item_dict[item]
            item_dict[item] = quantity + previous_quantity
        else:
            item_dict[item] = quantity

    sorted_dict = sorted(item_dict.items(), key=lambda kv: kv[1], reverse=True)
    item_dict =dict(sorted_dict)
    
    print(item_dict)
    filter = SaleFilter(request.GET, queryset = orders)    
    orders = filter.qs

    context = {'orders' : orders, 'items' : orderitems, 'filter' : filter, 'item_dict' : item_dict}
    return render(request, 'dashboard.html', context)


class JsonView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = SaleSerializer