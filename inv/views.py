from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello, world. You're at the inventory index.")

def dash(request):
    return HttpResponse("Hello, world. You're at the Dashboard.")

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


