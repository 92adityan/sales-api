import django_filters
from .models import Sale

class SaleFilter(django_filters.FilterSet):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['customer']