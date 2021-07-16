from django.shortcuts import render
from .models import OrderItem, Order, Customer
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import SaleSerializer
from .forms import OrderForm, OrderItemForm

def dashboard_view(request):

    orderitems = OrderItem.objects.all()
    orders = Order.objects.all()
    customers = Customer.objects.all()

    order_form = OrderForm()
    order_item_form = OrderItemForm()
    
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
    
    context = {'orders' : orders, 'items' : orderitems, 'filter' : filter, 
    'item_dict' : item_dict, 'order_item_form' : order_item_form, 'order_form' : order_form}
 
    return render(request, 'dashboard.html', context)


def create_order(request):
    if request.method == 'POST':
        new_order = OrderForm(request.POST)
        if new_order.is_valid:
            new_order.save()
            return HttpResponseRedirect('/')

def create_order_item(request):
    if request.method == 'POST':
        order_item_form = OrderItemForm(request.POST)
        if order_item_form.is_valid():
            order_item_form.save()
            return HttpResponseRedirect('/')


class JsonView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = SaleSerializer