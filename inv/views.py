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

def items(request):
    items = Items.objects.all()
    return render(request, 'inv/items.html', {'items' : items})

def item(request):
    return HttpResponse("Hello, world. You're looking at an individual item.")

def boxes(request):
    boxes = Boxes.objects.all()
    items = Items_in_boxes.objects.filter(date_to__exact='')
    return render(request, 'inv/boxes.html', {'boxes' : boxes, 'items' : items})

def box(request):
    return HttpResponse("Hello, world. You're looking at an individual box.")

def warehouses(request):
    boxes = Boxes.objects.all()
    wh = Warehouse.objects.all()
    return render(request, 'inv/warehouses.html', {'wh' : wh, 'boxes' : boxes})

def warehouse(request):
    return HttpResponse("Hello, world. You're looking at an individual warehouse.")

def consumable(request):
    consumables = Items.filter(item_consumable=True)
    return render(request, 'inv/consumables.html', {'consumables' : consumables})

def inventories(request):
    return HttpResponse("Hello, world. You're at the Inventories Summary.")

def inventory(request):
    return HttpResponse("Hello, world. You're looking at an individual summary.")
