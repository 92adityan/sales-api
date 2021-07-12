from django.shortcuts import render
from .models import OrderItem, Order
import datetime
from rest_framework import viewsets
from .serializers import SaleSerializer


def dashboard_view(request):
    orderitems = OrderItem.objects.all()
    orders = Order.objects.all()

    # top sold products
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

    # search by date  
    date_query = request.GET.get('date')
    if date_query != '' and date_query is not None:
        orders = Order.objects.filter(date = date_query)
    
    # search by order ID
    order_id_query = request.GET.get('order_id')
    if order_id_query != '' and order_id_query is not None:
        orders = Order.objects.filter(order_id__iexact = order_id_query)
    
    context = {'orders' : orders, 'items' : orderitems, 'filter' : filter, 'item_dict' : item_dict}
    return render(request, 'dashboard.html', context)


class JsonView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = SaleSerializer