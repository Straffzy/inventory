from django.contrib import admin
from . models import Warehouse, Staff, Boxes, Items, Items_in_boxes, Keywords, Keywords_in_items, Inventory

class WarehouseInLine(admin.TabularInline):
    model = Boxes
    extra = 1

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_name', 'warehouse_loc')
    inlines = [WarehouseInLine,]
    extra = 1

class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_title')
    extra = 1

class BoxesAdmin(admin.ModelAdmin):
    list_display = ('box_id', 'warehouse', 'box_description')
    extra = 1

class ItemsInLine(admin.TabularInline):
    model = Items_in_boxes
    extra = 1

class Keywords_Items(admin.TabularInline):
    model = Keywords_in_items
    extra = 1

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_desc', 'item_value')
    inlines = [ItemsInLine, Keywords_Items]
    extra = 1

class Items_in_boxesAdmin(admin.ModelAdmin):
    list_display = ('box_id', 'item_id', 'date_from', 'date_to', 'moved_by_staff_id', 'reason')
    extra = 1

class Keywords_itemsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'keyword')
    extra = 1

admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Boxes, BoxesAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Items_in_boxes, Items_in_boxesAdmin)
admin.site.register(Keywords)
admin.site.register(Keywords_in_items, Keywords_itemsAdmin)
admin.site.register(Inventory)



# Register your models here.


