from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dash/', views.dash, name='dashboard'),
        path('search/', views.search, name='search'),
        path('reports/', views.reports, name='reports'),
        path('items/', views.items, name='items'),
        path('items/<int:itemid>/', views.item, name='item'),
        path('boxes/', views.boxes, name='boxes'),
        path('boxes/<int:boxid>/', views.box, name='box'),
        path('warehouses/', views.warehouses, name='warehouses'),
        path('warehouses/<int:whid>/', views.warehouse, name='warehouse'),
        path('consumable/', views.consumable, name='consumable'),
        path('inventories/', views.inventory, name='inventories'),
        path('inventories/<int:invid>/', views.inventory, name='inventory'),
        path('keywords/', views.keywords, name='keywords'),
        path('downloads/', views.downloads, name='downloads'),
        ]
