from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=100, default='warehouse')
    warehouse_loc = models.CharField(max_length=200, blank=True)
    warehouse_details = models.CharField(max_length=300, blank=True)
    warehouse_img = models.CharField(max_length=20, blank=True, default='warehouse.png')
    class Meta: verbose_name_plural = "Warehouses"
    def __str__(self):
        return '%s' % (self.warehouse_name)

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_title = models.CharField(max_length=50, blank=True)
    staff_contact = models.CharField(max_length=100, blank=True)
    class Meta: verbose_name_plural = "Staff"
    def __str__(self):
        return '%s | %s' % (self.staff_name, self.staff_title)

class Boxes(models.Model):
    box_id = models.IntegerField(primary_key=True)
    box_name = models.CharField(max_length=20, default='box')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    box_location = models.CharField(max_length=300, blank=True)
    box_description = models.CharField(max_length=300, blank=True)
    other_box_details = models.CharField(max_length=300, blank=True)
    box_img = models.CharField(max_length=20, blank=True, default='box.png')
    class Meta: verbose_name_plural = "Boxes"
    def __str__(self):
        return '%s) %s' % (self.box_id, self.box_name)

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, default='name')
    item_owner_staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    item_desc = models.CharField(max_length=500, blank=True)
    item_img = models.CharField(max_length=50, blank=True)
    item_qty = models.IntegerField(default='1')
    item_value = models.DecimalField(max_digits=8,decimal_places=2, blank=True)
    item_consumable = models.BooleanField(default=False)
    item_remaining = models.IntegerField(
            verbose_name='Percent Remaining',
            default=100,
            validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
            )
    
    class Meta: verbose_name_plural = "Items"


class Items_in_boxes(models.Model):
    txn_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    box_id = models.ForeignKey(Boxes, on_delete=models.CASCADE)
    date_from = models.DateField(default=datetime.date.today)
    date_to = models.DateField(blank=True, null=True)
    moved_by_staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    class Meta: verbose_name_plural = "Items in Boxes"

class Keywords(models.Model):
    keyword = models.CharField(primary_key=True, max_length=50)
    keyword_desc = models.CharField(max_length=100, blank=True)
    class Meta: verbose_name_plural = "Keywords"
    def __str__(self):
        return '%s' % (self.keyword)

class Keywords_in_items(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    class Meta: verbose_name_plural = "Keywords in Items"

class Inventory(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_date = models.DateField(default=datetime.date.today)
    inv_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True)
    inv_box = models.ForeignKey(Boxes, on_delete=models.CASCADE, blank=True)
    inv_item = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True)
    inv_comment = models.CharField(max_length=500)
    class Meta: verbose_name_plural = "Inventories"
    def __str__(self):
        return '%s' % (self.inv_date, inv_comment)

