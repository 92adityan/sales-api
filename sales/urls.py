from django.urls import path, include
from .views import dashboard_view,JsonView
from rest_framework import routers

router =routers.DefaultRouter()
router.register('sales', JsonView)

urlpatterns = [
    path('dashboard/', dashboard_view, name = 'dashboard'),
    path('api/', include(router.urls))
]