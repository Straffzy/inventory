from django.shortcuts import render
from django.http import HttpResponse
from .models import Warehouse, Boxes, Items, Staff, Items_in_boxes, Keywords, Keywords_in_items, Inventory
from django.db.models import Count, Sum
def index(request):
    item_count = Items.objects.all().annotate(Count("item_id"))
    box_count = Boxes.objects.all().annotate(Count("box_id"))
    warehouse_count = Warehouse.objects.all().annotate(Count("warehouse_id"))
    val = Items.objects.all().aggregate(Sum("item_value"))
    return render(request, 'inv/index.html', {'item_count' : item_count, 'box_count' : box_count, 'warehouse_count' : warehouse_count, 'val' : val })

def dash(request):
    return render(request, 'inv/dash.html', {})

def search(request):
    return HttpResponse("Hello, world. You're at the Search Page.")

def reports(request):
    return HttpResponse("Hello, world. You're at the Reports Page.")

def item(request):
    return HttpResponse("Hello, world. You're at the Item Page.")

def box(request):
    return HttpResponse("Hello, world. You're at the Box Page.")

def warehouse(request):
    return HttpResponse("Hello, world. You're at the Warehouse Page.")

def consumable(request):
    return HttpResponse("Hello, world. You're at the Consumables Page.")

def inventory(request):
    return HttpResponse("Hello, world. You're at the Inventories Page.")
