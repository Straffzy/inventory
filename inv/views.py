from django.shortcuts import render
from django.http import HttpResponse
from .models import Warehouse, Boxes, Items, Staff, Items_in_boxes, Keywords, Keywords_in_items, Inventory
from django.db.models import Count, Sum, Q, F, FloatField 

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

def item(request, itemid):
    item = Items.objects.get(box_id=itemid)
    box = Items_in_boxes.objects.filter(date_to__isnull=True).filter(itemid)
    wh = Warehouses.objects.get(items_in_boxes__box_id__warehouse)
    return render(request, 'inv/item.html', {'item' : item, 'box' : box, 'wh' : wh}) 

def boxes(request):
    curr_items = Items_in_boxes.objects.filter(date_to__isnull=True)
    boxes = Boxes.objects.all().annotate(num_items=Count('curr_items'))
    return render(request, 'inv/boxes.html', {'boxes' : boxes })

def box(request, boxid):
    box = Boxes.objects.prefetch_related('warehouse').get(box_id=boxid)
    items = Items_in_boxes.objects.prefetch_related().filter(date_to__isnull=True).filter(box_id=boxid).annotate(totval=Sum(F('item_id__item_value')*F('item_id__item_qty'),
        output_field=FloatField()), item_img=F('item_id__item_img'))
    val = Items_in_boxes.objects.filter(box_id=boxid).filter(date_to__isnull=True).aggregate(Sum("item_id__item_value"))
    return render(request, 'inv/box.html', {'box' : box, 'items': items, 'val' : val})

def warehouses(request):
    wh = Warehouse.objects.all().annotate(num_boxes=Count('boxes'))
    return render(request, 'inv/warehouses.html', {'wh' : wh})

def warehouse(request, whid):
    wh = Warehouse.objects.get(warehouse_id=whid)
    boxes = Boxes.objects.filter(warehouse_id=whid).annotate(num_items=Count('items_in_boxes',
        filter=Q(items_in_boxes__date_to__isnull=True))).annotate(val=Sum("items_in_boxes__item_id__item_value",
            filter=Q(items_in_boxes__date_to__isnull=True)))
    return render(request, 'inv/warehouse.html', {'wh' : wh, 'boxes' : boxes})

def consumable(request):
    consumables = Items.filter(item_consumable=True)
    return render(request, 'inv/consumables.html', {'consumables' : consumables})

def inventories(request):
    return HttpResponse("Hello, world. You're at the Inventories Summary.")

def inventory(request, invid):
    return HttpResponse("Hello, world. You're looking at an individual inventory summary.")

def keywords(request):
    return HttpResponse("Hello, world. You're looking at a list of keywords.")

def downloads(request):
    return HttpResponse("Hello, world. You're looking at the Downloads Page.")
