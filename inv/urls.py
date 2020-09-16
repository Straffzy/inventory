from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dash', views.dash, name='dashboard'),
        path('search', views.search, name='search'),
        path('reports', views.reports, name='reports'),
        path('items', views.items, name='items'),
        path('items/<item_id>', views.item),
        path('boxes', views.boxes, name='boxes'),
        path('boxes/<box_id>', views.box),
        path('warehouses', views.warehouses, name='warehouses'),
        path('warehouses/<warehouse_id>', views.warehouse),
        path('consumable', views.consumable),
        path('inventories', views.inventory, name='inventories'),
        path('inventories/<inventory_id', views.inventory),
        ]
