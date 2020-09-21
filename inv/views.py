from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Warehouse, Boxes, Items, Staff, Items_in_boxes, Keywords, Keywords_in_items, Inventory
from django.db.models import Count, Sum, Q, F, DecimalField, FloatField, IntegerField, ExpressionWrapper
from decimal import Decimal
from django.db.models.functions import Lower

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
    return render(request, 'inv/reports.html')

def report_itm(request, item_sort=None):
    # item_sort 1 is alpha by item_name
    if item_sort == 1:
        items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    # item_sort 2 is by item_id
    elif item_sort == 2:
         items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).order_by('item_id')
    else:   
         items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField()))
    return render(request, 'inv/rpt_items.html', {'items' : items})
    
def report_box(request, box=None):
    if box:
        boxes = Boxes.objects.filter(box_id=box)
    else: 
        boxes = Boxes.objects.all()
    items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    return render(request, 'inv/rpt_boxes.html', {'items' : items, 'boxes' : boxes})

def report_wh(request, whid=None):
    # warehouse report for a single warehouse
    if whid:
        wh = Warehouse.objects.filter(warehouse_id=whid)
    else: wh = Warehouse.objects.all()
    box = Boxes.objects.all().prefetch_related().annotate(whid=F('warehouse__warehouse_id'))
    items =  items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    
    return render(request, 'inv/rpt_wh.html', {'items' : items, 'wh' : wh, 'box' : box})

def items(request):
    items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    return render(request, 'inv/items.html', {'items' : items})

def item(request, itemid):
    item = Items.objects.filter(item_id=itemid).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).get(item_id=itemid)
    box = Items_in_boxes.objects.filter(item_id=itemid).filter(date_to__isnull=True).annotate(name=F('box_id__box_name')).annotate(bx_id=F('box_id')).get(item_id=itemid) 
    wh = Boxes.objects.filter(box_id=box.bx_id).annotate(name=F('warehouse__warehouse_name')).get(box_id=box.bx_id)
    return render(request, 'inv/item.html', {'item' : item , 'box' : box, 'wh' : wh }) 

def boxes(request):
    boxes = Boxes.objects.all().annotate(num_items=Count('bx_id__item_id', filter=Q(bx_id__date_to__isnull=True)))
    return render(request, 'inv/boxes.html', {'boxes' : boxes })

def box(request, boxid):
    box = Boxes.objects.prefetch_related('warehouse').get(box_id=boxid)
    items = Items_in_boxes.objects.prefetch_related().filter(date_to__isnull=True).filter(box_id=boxid).annotate(item_img=F('item_id__item_img'), totval=Sum(F('item_id__item_value')*F('item_id__item_qty'), output_field=FloatField()))
    items.item_totals = Items_in_boxes.objects.filter(date_to__isnull=True).filter(box_id=boxid).aggregate(icount=Count('item_id'), val=Sum('item_id__item_value'))
    return render(request, 'inv/box.html', {'box' : box, 'items': items})

def warehouses(request):
    wh = Warehouse.objects.all().annotate(num_boxes=Count('bx_wh'))
    return render(request, 'inv/warehouses.html', {'wh' : wh})

def warehouse(request, whid):
    wh = Warehouse.objects.get(warehouse_id=whid)
    boxes = Boxes.objects.filter(warehouse_id=whid).annotate(num_items=Count('bx_id',
        filter=Q(bx_id__date_to__isnull=True))).annotate(val=Sum("bx_id__item_id__item_value",
            filter=Q(bx_id__date_to__isnull=True)))
    return render(request, 'inv/warehouse.html', {'wh' : wh, 'boxes' : boxes})

def consumables(request):
    consumables = Items.objects.filter(item_consumable=True).annotate(restock=ExpressionWrapper(F('item_qty') * ((100.0 - F('item_remaining'))/100.0), output_field=FloatField()))
    return render(request, 'inv/consumables.html', {'consumables' : consumables})

def inventories(request):
    return HttpResponse("Hello, world. You're at the Inventories Summary.")

def inventory(request, invid):
    return HttpResponse("Hello, world. You're looking at an individual inventory summary.")

def keywords(request):
    return HttpResponse("Hello, world. You're looking at a list of keywords.")

########## PDF Generation Classes ##############

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

def titlePage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75*inch, "First Page")
    canvas.restoreState()

def regPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75*inch, "Page %d " % doc.page)
    canvas.restoreState()

def fullpdf(request):
    import io 
    from datetime import date
    from reportlab.pdfgen import canvas
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch

    # set up the document
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename=file.pdf'

    buff = io.BytesIO()


    PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
    styles = getSampleStyleSheet()
    filename = ("full_inventory.%s.pdf" % date.today())
    doc = SimpleDocTemplate(filename)
    story = [Spacer(1,2*inch)]
    style = styles['Normal']
    tstyle = styles['Title']
    Title = Paragraph("Inventory Report", tstyle)
    Subtitle = Paragraph("Table of contents <br/> <ol><li>Box List by ID</li><li>Box List by Name</li><li>Items by Box, ordered by Warehouse</li></ul>", style)
    story.append(Title)
    story.append(Subtitle)
    # generate the boxes by ID table
    boxes_bxid = Boxes.objects.all().order_by('box_id')
    desc = ("Boxes ordered by Box ID")
    p = Paragraph(desc, style)
    story.append(p)
    for b in boxes_bxid:
        boxid = "ID"
        name = "Name"
        data = [boxid, name]
        row = [b.box_id, b.box_name]
        data.append(row)
    t = Table(data, splitByRow=1, repeatRows=0)
    story.append(t)
    story.append(PageBreak())

    # generate the boxes by name table
    boxes_bxnm = Boxes.objects.all().annotate(iname=Lower('box_name')).order_by('iname') 
    desc = ("Boxes ordered by Box Name")
    p = Paragraph(desc, style)
    story.append(p)
    for b in boxes_bxnm:
        boxid = "ID"
        name = "Name"
        data = [boxid, name]
        row = [b.box_id, b.box_name]
        data.append(row)
    t = Table(data, splitByRow=1, repeatRows=0)
    story.append(t)
    story.append(PageBreak())

    # generate the items by box tables, sorted by warehouse
    boxes_whid = Boxes.objects.all().prefetch_related().annotate(wh=F('warehouse__warehouse_name')).order_by('warehouse')
    items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    for b in boxes_whid:
        desc = ("%s: %s in %s" % (b.box_id, b.box_name, b.wh))
        p = Paragraph(desc, style)
        story.append(p)
        boxid = "ID"
        name = "Name"
        desc = "Description"
        qty = "Quantity"
        val = "Value (ea)"
        totval = "Value (tot)"
        percent = "Percent Rem."
        data = [boxid, name, desc, qty, val, totval, percent]
        for i in items:
            if i.boxid == b.box_id:
                row = [i.item_id, i.item_name, i.item_desc, i.item_qty, round(i.item_value, 2), round(i.totval, 2), i.item_remaining]
                data.append(row)
        t = Table(data, splitByRow=1, repeatRows=0)
        story.append(t)
        story.append(PageBreak())
    doc.build(story, onFirstPage=titlePage, onLaterPages=regPage)
    response.write(buff.getvalue())
    buff.close()
    return response
                
