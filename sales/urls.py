from django.urls import path, include
from .views import create_order_item, dashboard_view,JsonView, create_order
from rest_framework import routers

router =routers.DefaultRouter()
router.register('sales', JsonView)

urlpatterns = [
    path('', dashboard_view, name = 'dashboard'),
    path('create-order/', create_order, name = 'create-order'),
    path('create-order-item/', create_order_item, name = 'create-order-item'),
    path('api/', include(router.urls))
]