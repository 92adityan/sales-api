from django.shortcuts import render
from .models import Sale

def dashboard_view(request):
    sales = Sale.objects.all()
    context = {'sales' : sales}

    if request.method == 'GET':
        search_date = request.GET.get('date')
        print(search_date)
    return render(request, 'dashboard.html', context)