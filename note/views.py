from operator import gt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from django.core.serializers import serialize
from django.http import JsonResponse
from json import loads
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from django.db.models import Q

from .models import Client, Cost, Note, Noteitem, Location, Notekey, Notetype, Status, Noteitemkey, PO, POItem, PR, PRItem, Product, SO, SOItem, SR, SRItem, CO, COItem, WI, WR, WIItem, WRItem, Inv, InvControl, WorkInvControl

def notes(request):
    
    notes = None
    
    notetype = request.GET.get('notetype', '')
    client = request.GET.get('client', '')
    location = request.GET.get('location', '')

    # One day old notes not displayed
    
    # creationDate = datetime.datetime.now()
    todayDate = timezone.now()
    
    if notetype or client:
        if notetype and client and location:
            notes = Note.objects.filter(notetype_id=notetype, created_on__date=todayDate, client_id=client, location_id=location)
        if notetype and client and location:
            notes = Note.objects.filter(notetype_id=notetype, created_on__date=todayDate, client_id=client, location_id=location)
        if notetype and client=='' and location =='':
            notes = Note.objects.filter(notetype_id=notetype, created_on__date=todayDate)
        if notetype and location and client=='':
            notes = Note.objects.filter(notetype_id=notetype, created_on__date=todayDate, location_id=location)
        if notetype and location=='' and client:
            notes = Note.objects.filter(notetype_id=notetype, created_on__date=todayDate, client_id=client)
        if notetype=="" and client:
            notes = Note.objects.filter(client_id=client, created_on__date=todayDate)
        if notetype=="" and client and location:
            notes = Note.objects.filter(client_id=client, created_on__date=todayDate, location_id=location)
        #return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients, 'locations': locations, 's_notetype': s_notetype})
    
    return render(request, 'note/notes.html', {'notes': notes})

    
''' def notes(request):
    
    selected = {}
    notes = None
    client = None
    location = None
    s_notetype = None
    
    if request.method == 'GET':
        s_notetype = request.GET.get('notetype', '')
        client = request.GET.get('client', '')
        location = request.GET.get('location', '')

        selected['client']=client
        selected['location']=location
        selected['notetype']=s_notetype
    
        if s_notetype or client:
            if s_notetype and client and location:
                notes = Note.objects.filter(notetype_id=s_notetype, client_id=client, location_id=location)
            if s_notetype and client=="":
                notes = Note.objects.filter(notetype_id=s_notetype)
            if s_notetype and location and client=="":
                notes = Note.objects.filter(notetype_id=s_notetype, location_id=location)
            if s_notetype=="" and client:
                notes = Note.objects.filter(client_id=client)
            if s_notetype=="" and client and location:
                notes = Note.objects.filter(client_id=client, location_id=location)
            #return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients, 'locations': locations, 's_notetype': s_notetype})
            return render(request, 'note/notes.html', {'notes': notes})

    notetypes = Notetype.objects.all()
    clients = Client.objects.all()
    locations = Location.objects.all()

    return render(request, 'note/init.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients, 'locations': locations, 's_notetype': s_notetype, 'selected': selected})
 '''
def init(request):
    notetypes = Notetype.objects.all()
    clients = Client.objects.all()
    locations = Location.objects.all()
    notes = None
    return render(request, 'note/init.html', {'notes': notes, 'notetypes': notetypes, 'locations': locations, 'clients': clients })

@require_http_methods(['POST'])
def add_note(request):
    note = None
    obj_note = None
    notetype = request.POST.get('notetype', '')
    location = request.POST.get('location', '')
    notekey = request.POST.get('notekey', '')
    client = request.POST.get('client', '')
    
    my_dict = {'notetype': notetype, 'client': client, 'location': location, 'notekey': notekey}  # Your dict with fields
    msg=""
    for key, value in my_dict.items():
        if value=="":
            msg=msg + key + " "
        
    if notekey and notetype!=None and client:
        obj_notetype = Notetype.objects.get(id=notetype)
        obj_notekey, create_notekey = Notekey.objects.get_or_create(notekey=notekey)
        obj_client = Client.objects.get(id=client)
        
        if obj_notetype.id == 1:
            obj_po, create_po = PO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_po.note_ptr_id)

        if obj_notetype.id == 11:
            obj_po, create_po = PR.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_po.note_ptr_id)

        if obj_notetype.id == 2:
            obj_so, create_so = SO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_so.note_ptr_id)

        if obj_notetype.id == 12:
            obj_so, create_so = SR.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_so.note_ptr_id)

        if obj_notetype.id == 3:
            obj_co, create_po = CO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_co.note_ptr_id)

        if obj_notetype.id == 4:
            obj_wo, create_so = WI.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_wo.note_ptr_id)

        if obj_notetype.id == 14:
            obj_wo, create_so = WR.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_wo.note_ptr_id)
                   
    return render(request, 'note/partials/note.html', {'note': obj_note, 'msg': msg})

@require_http_methods(['GET', 'POST'])
def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.notetype = request.POST.get('notetype', '')
        note.save()

        return render(request, 'note/partials/note.html', {'note': note})
    
    return render(request, 'note/partials/edit_note.html', {'note': note})

@require_http_methods(['PUT'])
def update_note(request, pk):

    note = Note.objects.get(id=pk)
    status = Status.objects.get(id=2)
    
    note.is_final = True
    note.status = status
    note.save()

    return render(request, 'note/partials/note.html', {'note': note})

@require_http_methods(['DELETE'])
def delete_note(request, pk):
    
    note = Note.objects.get(id=pk)
    
    note.delete()

    return HttpResponse()


def noteitems(request, pk):
    #notekey = Notekey.objects.get(notekey=noteref)
    note = Note.objects.get(id=pk)
    invlist=None
    message=None

    products = Product.objects.all()
    noteref = note.notekey_id
    noteitems = Noteitem.objects.filter(notekey_id=noteref, notetypekey_id=note.notetype_id)

    # if note.notetype_id==1 and request.method == 'GET' and request.GET.get('product', ''):
    #     invlist = Inv.objects.filter(product_id=request.GET.get('product', ''))

    #note = Note.objects.filter(notekey_id=notekey)[:1].get()

    return render(request, 'note/noteitems.html', {'noteref': noteref, 'noteitems': noteitems, 'note': note, 'products': products, 'invlist': invlist, 'message' : message})

@require_http_methods(['GET', 'POST'])
def invlist(request, pk):
    message=None
    note = Note.objects.get(id=pk)
    #invlist = Inv.objects.filter(product_id=request.GET.get('product', ''))
    product=request.GET.get('product', '')
    prodcost=request.GET.get('prodcost', '')
    weight=request.GET.get('weight', '')
    qty=request.GET.get('qty', '')
    if weight=='':
        weight=1
    if qty=='':
        qty=1
    obj_product=Product.objects.get(pk=product)
    invlist = InvControl.objects.filter(product_id=request.GET.get('product', ''), inventory__gt =0 )
    cost=Cost.objects.filter(carat_id=obj_product.carat_id).first()
    rate=obj_product.sell_rate
    if note.notetype.id == 1:
        rate=obj_product.buy_rate
    prodcost=cost.cost+(cost.cost/100*rate)
    icost=prodcost*qty*weight
    return render(request, 'note/invlist.html', {'note': note, 'invlist':invlist, 'message' : message, 'prodcost' : prodcost, 'weight': weight, 'qty': qty, 'icost': icost})

# @require_http_methods(['GET', 'POST'])
# def invdata(request):
#     message=None
#     weight = request.POST.get('weight', '')
#     quantity = request.POST.get('quantity', '')
#     if '-' in weight:
#         s_invitem = weight.split('-')[2]
#         obj_invcontrol=InvControl.objects.get(id=s_invitem)
#         if int(quantity) > obj_invcontrol.inventory:
#             message = "Maximum Quantity exceeded"
#     #return HttpResponse(error)
#     return render(request, 'note/partials/message.html', {'message': message})

# @require_http_methods(['GET', 'POST'])
# def val_qty(request):
#     message=None
#     weight = request.POST.get('weight', '')
#     qty = request.POST.get('qty', '')
#     if qty=='' or qty==0:
#         message = "Quantity is mandatory!"
#         return render(request, 'note/partials/message.html', {'message': message})

#     if '-' in weight:
#         s_invitem = weight.split('-')[2]
#         obj_invcontrol=InvControl.objects.get(id=s_invitem)
#         if int(qty) > obj_invcontrol.inventory:
#             message = "Maximum Quantity Exceeded!"
#     #return HttpResponse(message)
#     return render(request, 'note/partials/message.html', {'message': message})

# @require_http_methods(['GET', 'POST'])
# def val_cost(request):
#     message=None
#     weight = request.POST.get('weight', '')
#     cost = request.POST.get('cost', '')
#     if '-' in weight:
#         s_invitem = weight.split('-')[2]
#         obj_invcontrol=InvControl.objects.get(id=s_invitem)
#         if float(cost) <= obj_invcontrol.noteitem.cost:
#             message = "Cost less than purchased!"
#     #return HttpResponse(message)
#     return render(request, 'note/partials/message.html', {'message': message})

@require_http_methods(['GET', 'POST'])
def icost(request, pk):
    note = Note.objects.get(id=pk)
    message=None
    product=request.POST.get('product', '')
    prodcost=request.POST.get('prodcost', '')
    weight = request.POST.get('weight', '')
    icost = request.POST.get('icost', '')
    qty = request.POST.get('qty', '')

    if weight=='' or weight==0:
        weight=1
    if qty=='' or qty==0:
        qty=1
        
    if qty=='' or qty==0:
        message = "Quantity is mandatory!"
        return render(request, 'note/partials/message.html', {'message': message, 'note': note})

    wgt=weight

    if '-' in weight:
        s_invitem = weight.split('-')[2]
        wgt = weight.split('-')[0]
        obj_invcontrol=InvControl.objects.get(id=s_invitem)
        if int(qty) > obj_invcontrol.inventory:
            message = "Maximum Quantity Exceeded!"
        #if float(icost) <= obj_invcontrol.noteitem.cost:
        #    message = "Cost less than purchased!"
    
    #weight=float(weight)
    #qty=int(qty)
    obj_product=Product.objects.get(pk=product)
    invlist = InvControl.objects.filter(product_id=product, inventory__gt =0 )
    cost=Cost.objects.filter(carat_id=obj_product.carat_id).first()
    rate=obj_product.sell_rate
    if note.notetype.id == 1:
        rate=obj_product.buy_rate
        prodcost=cost.cost+(cost.cost/100*rate)
    if note.notetype.id == 2:
        rate=obj_product.sell_rate
        prodcost=cost.cost+(cost.cost/100*rate)
    icost=prodcost*int(qty)*Decimal(wgt) 
    return render(request, 'note/invlist.html', {'note': note, 'weight': weight, 'invlist':invlist, 'message' : message, 'prodcost' : prodcost, 'qty': qty, 'icost': icost})
        

# @require_http_methods(['GET', 'POST'])
# def val_icost(request, pk):
#     note = Note.objects.get(id=pk)
#     message=None
#     product=request.POST.get('product', '')
#     prodcost=request.POST.get('prodcost', '')
#     wgt = weight = request.POST.get('weight', '')
#     icost = request.POST.get('icost', '')
#     qty = request.POST.get('qty', '')

#     if weight=='' or weight==0:
#         weight=1
#     if qty=='' or qty==0:
#         qty=1
        
#     if qty=='' or qty==0:
#         message = "Quantity is mandatory!"
#         return render(request, 'note/partials/message.html', {'message': message})

#     if '-' in weight:
#         s_invitem = weight.split('-')[2]
#         wgt = weight.split('-')[0]
#         obj_invcontrol=InvControl.objects.get(id=s_invitem)
#         if int(qty) > obj_invcontrol.inventory:
#             message = "Maximum Quantity Exceeded!"
#         #if float(icost) <= obj_invcontrol.noteitem.cost:
#         #    message = "Cost less than purchased!"
    
#     #weight=float(weight)
#     #qty=int(qty)
#     obj_product=Product.objects.get(pk=product)
#     #invlist = InvControl.objects.filter(product_id=product, inventory__gt =0 )
#     cost=Cost.objects.filter(carat_id=obj_product.carat_id).first()
#     rate=obj_product.sell_rate
#     if note.notetype.id == 1:
#         rate=obj_product.buy_rate
#         prodcost=cost.cost+(cost.cost/100*rate)
#     if note.notetype.id == 2:
#         rate=obj_product.sell_rate
#         prodcost=cost.cost+(cost.cost/100*rate)
#     icost=Decimal(prodcost)*int(qty)*Decimal(wgt) 
#     return render(request, 'note/partials/icost.html', {'message' : message, 'prodcost' : prodcost, 'qty': qty, 'icost': icost})


@require_http_methods(['GET', 'POST'])
def edit_noteitem(request, pk):
    #notekey = Notekey.objects.get(notekey=note)
    #obj_notetype = Notetype.objects.get(id=note.notetype)
    noteitem = Noteitem.objects.get(id=pk)

    if request.method == 'POST':
        product = request.POST.get('product', '')
        noteitem.product=Product.objects.get(product_name=product)
        noteitem.quantity = request.POST.get('quantity', '')
        noteitem.cost = request.POST.get('cost', '')
        noteitem.weight = request.POST.get('weight', '')
        noteitem.save()
  
        #note = Note.objects.filter(notekey_id=notekey)[:1].get()

        return render(request, 'note/partials/noteitem.html', {'noteitem': noteitem})
    
    return render(request, 'note/partials/edit_noteitem.html', {'noteitem': noteitem})

@require_http_methods(['POST'])
def add_noteitem(request, note):
    noteitem = None
    obj_item=''
    message = None
    product=request.POST.get('product', '')
    prodcost=request.POST.get('prodcost', '')
    weight = request.POST.get('weight', '')
    #icost = request.POST.get('icost', '')
    quantity = request.POST.get('qty', '')
    
    if product=='' or prodcost=='' or quantity=='' or weight=='' or note==None:
        message="Incomplete data"
        return render(request, 'note/partials/message.html', {'message': message})

    if '-' in weight:
        s_noteitem = weight.split('-')[1]
        s_invitem = weight.split('-')[2]
        weight = weight.split('-')[0]
        obj_invcontrol=InvControl.objects.get(id=s_invitem)
        #if float(icost) <= obj_invcontrol.noteitem.cost:
            #message="Invalid Cost data"
            #return HttpResponse(message)
            #return render(request, 'note/partials/message.html', {'message': message})
        if int(quantity) > obj_invcontrol.inventory:
            message = "Maximum Quantity Exceeded!"
            return render(request, 'note/partials/message.html', {'message': message})

    note = Note.objects.get(id=note)
    obj_product=Product.objects.get(pk=product)
    #invlist = InvControl.objects.filter(product_id=product, inventory__gt =0 )
    cost=Cost.objects.filter(carat_id=obj_product.carat_id).first()
    rate=obj_product.sell_rate

    if cost=='' or rate=='':
        message = "Product cost or rate unavailable !"
        return render(request, 'note/partials/message.html', {'message': message})

    if note.notetype.id == 1:
        rate=obj_product.buy_rate

    if note.notetype.id == 2:
        rate=obj_product.sell_rate
    
    costid = cost.id
    # product rate
    prate=cost.cost+(cost.cost/100*rate)
    # product cost
    pcost=prate*Decimal(weight)
    # total cost
    icost=pcost*int(quantity)

    obj_notekey = Notekey.objects.get(id=note.notekey_id)
    obj_notetype = Notetype.objects.get(id=note.notetype_id)
    obj_noteitemkey, create_noteitemkey = Noteitemkey.objects.get_or_create(notekey=obj_notekey)
        
    #obj_product = Product.objects.get(id=product)

    obj_invitem, create_invitem = Inv.objects.get_or_create(product=obj_product, weight=weight)

    # quantity based on inv
    qty = obj_invitem.item
    # qty based on invcontrol - by note/customer
    
    # Purchase
    if note.notetype_id == 1:
        qty = qty + int(quantity)
        #qtyc = qtyc + int(quantity)
        qtyz=int(quantity)
        obj_item, create_poitem = POItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            notetypekey=obj_notetype,
            product=obj_product,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)
    
    # Purchase Return
    if note.notetype_id == 11:
        qty = qty - int(quantity)
        #qtyc = qtyc - int(quantity)
        qtyz=-int(quantity)
        obj_item, create_poitem = PRItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            notetypekey=obj_notetype,
            product=obj_product,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)
        
    # Sales
    if note.notetype_id == 2:
        qty = qty - int(quantity)
        #qtyc = qtyc - int(quantity)
        qtyz=-int(quantity)
        obj_item, create_poitem = SOItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            product=obj_product,
            notetypekey=obj_notetype,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)
        obj_item=Noteitem.objects.get(id=s_noteitem)

    # Sales Return
    if note.notetype_id == 12:
        qty = qty + int(quantity)
        #qtyc = qtyc + int(quantity)
        qtyz=int(quantity)
        obj_item, create_poitem = SRItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            product=obj_product,
            notetypekey=obj_notetype,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)

    # Customer Orders
    if note.notetype_id == 3:
        obj_item, create_poitem = COItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            notetypekey=obj_notetype,
            product=obj_product,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)

    # Workshop Issues
    if note.notetype_id == 4:
        qty = qty - int(quantity)
        qtyz=-int(quantity)
        wtga = Decimal(weight) * int(quantity)
        obj_item, create_poitem = WIItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            product=obj_product,
            notetypekey=obj_notetype,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)
        obj_item=Noteitem.objects.get(id=s_noteitem)

    # Workshop Return
    if note.notetype_id == 14:
        qty = qty + int(quantity)
        qtyz=int(quantity)
        wtga = - Decimal(weight) * int(quantity)
        obj_item, create_poitem = WRItem.objects.get_or_create(
            noteitemkey=obj_noteitemkey,
            notekey=obj_notekey,
            product=obj_product,
            notetypekey=obj_notetype,
            quantity=quantity,
            weight=weight,
            note=note,
            costid=costid,
            prate=prate,
            pcost=pcost,
            icost=icost)

    if note.notetype_id != 3:
    
        obj_invcontrol, create_invcntitem = InvControl.objects.get_or_create(product=obj_product, weight=weight, noteitem=obj_item, defaults={'inv': obj_invitem})
        qtyc = obj_invcontrol.inventory
        qtyc = qtyc + qtyz
        obj_invitem.item = qty

        obj_invitem.item = qty
        obj_invitem.save()
        
        obj_invcontrol.inventory = qtyc
        obj_invcontrol.save()
    
    if note.notetype_id == 4 or note.notetype_id == 14:
        
        obj_workinvcontrol, create_invcntitem = WorkInvControl.objects.get_or_create(client_id=note.client_id)
        wtgc = obj_workinvcontrol.inventory
        wtgc = wtgc + wtga
        obj_workinvcontrol.inventory = wtgc

        obj_workinvcontrol.save()
    
    message='Item successfully added'
            
    return render(request, 'note/partials/noteitem.html', {'noteitem': obj_item, 'note': note, 'message': message})


@require_http_methods(['PUT'])
def update_noteitem(request, pk):

    # notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.is_final = True
    noteitem.save()

    return render(request, 'note/partials/noteitem.html', {'noteitem': noteitem})

@require_http_methods(['DELETE'])
def delete_noteitem(request, pk):
    
    #notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.delete()

    return HttpResponse()

