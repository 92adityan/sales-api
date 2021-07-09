from django.shortcuts import render
from .models import OrderItem, Sale
import datetime
from rest_framework import viewsets
from .serializers import SaleSerializer
from .filters import SaleFilter

def dashboard_view(request):
    orders = Sale.objects.all()
    items = OrderItem.objects.all()

    filter = SaleFilter(request.GET, queryset = orders)    
    orders = filter.qs

    context = {'orders' : orders, 'items' : items, 'filter' : filter}
    return render(request, 'dashboard.html', context)


class JsonView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer