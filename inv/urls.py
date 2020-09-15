from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dash', views.dash, name='dashboard'),
        path('search', views.search, name='search'),
        path('reports', views.reports, name='reports'),
        path('item', views.item),
        path('box', views.box),
        path('warehouse', views.warehouse),
        path('consumable', views.consumable),
        path('inventory', views.inventory, name='inventories'),
        ]
