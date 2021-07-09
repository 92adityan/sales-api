from django.shortcuts import render
from .models import OrderItem, Sale
import datetime
from rest_framework import viewsets
from .serializers import SaleSerializer

def dashboard_view(request):
    orders = Sale.objects.all()
    items = OrderItem.objects.all()
    context = {'orders' : orders, 'items' : items}

    if request.method == 'GET':
        pass
    return render(request, 'dashboard.html', context)


class JsonView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer