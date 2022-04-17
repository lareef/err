from operator import gt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Client, Note, Noteitem, Location, Notekey, Notetype, Status, Noteitemkey, PO, POItem, PR, PRItem, Product, SO, SOItem, SR, SRItem, CO, COItem, WI, WR, WIItem, WRItem, Inv, InvControl

def notes(request):
    
    notes = None
    
    notetype = request.GET.get('notetype', '')
    client = request.GET.get('client', '')
    location = request.GET.get('location', '')

    if notetype or client:
        if notetype and client and location:
            notes = Note.objects.filter(notetype_id=notetype, client_id=client, location_id=location)
        if notetype and client=='' and location =='':
            notes = Note.objects.filter(notetype_id=notetype)
        if notetype and location and client=='':
            notes = Note.objects.filter(notetype_id=notetype, location_id=location)
        if notetype and location=='' and client:
            notes = Note.objects.filter(notetype_id=notetype, client_id=client)
        if notetype=="" and client:
            notes = Note.objects.filter(client_id=client)
        if notetype=="" and client and location:
            notes = Note.objects.filter(client_id=client, location_id=location)
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
    notetype = request.POST.get('notetype', '')
    notekey = request.POST.get('notekey', '')
    client = request.POST.get('client', '')

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
                   
    return render(request, 'note/partials/note.html', {'note': obj_note})

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

    products = Product.objects.all()
    noteref = note.notekey_id
    noteitems = Noteitem.objects.filter(notekey_id=noteref, notetypekey_id=note.notetype_id)

    # if note.notetype_id==1 and request.method == 'GET' and request.GET.get('product', ''):
    #     invlist = Inv.objects.filter(product_id=request.GET.get('product', ''))

    #note = Note.objects.filter(notekey_id=notekey)[:1].get()

    return render(request, 'note/noteitems.html', {'noteref': noteref, 'noteitems': noteitems, 'note': note, 'products': products, 'invlist': invlist})

@require_http_methods(['GET', 'POST'])
def invlist(request):
    #invlist = Inv.objects.filter(product_id=request.GET.get('product', ''))
    invlist = InvControl.objects.filter(product_id=request.GET.get('product', ''), inventory__gt =0 )
    return render(request, 'note/invlist.html', {'invlist':invlist})

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
    #invlist = None
    product = request.POST.get('product', '')
    quantity = request.POST.get('quantity', '')
    cost = request.POST.get('cost', '')
    weight = request.POST.get('weight', '').split('-')[0]
    s_noteitem = request.POST.get('weight', '').split('-')[1]

    if note:
        note = Note.objects.get(id=note)
        obj_notekey = Notekey.objects.get(id=note.notekey_id)
        obj_notetype = Notetype.objects.get(id=note.notetype_id)
        obj_noteitemkey, create_noteitemkey = Noteitemkey.objects.get_or_create(notekey=obj_notekey)
        if product:
            obj_product = Product.objects.get(id=product)

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
                    cost=cost)
            
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
                    cost=cost)
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
                    cost=cost)
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
                    cost=cost)

            # Customer Orders
            if note.notetype_id == 3:
                obj_item, create_poitem = COItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    notetypekey=obj_notetype,
                    product=obj_product,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)

            # Workshop Issues
            if note.notetype_id == 4:
                qty = qty - int(quantity)
                #qtyc = qtyc - int(quantity)
                qtyz=-int(quantity)
                obj_item, create_poitem = WIItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    product=obj_product,
                    notetypekey=obj_notetype,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)

            # Workshop Return
            if note.notetype_id == 14:
                qty = qty + int(quantity)
                #qtyc = qtyc + int(quantity)
                qtyz=int(quantity)
                obj_item, create_poitem = WRItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    product=obj_product,
                    notetypekey=obj_notetype,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)


            obj_invcontrol, create_invcntitem = InvControl.objects.get_or_create(product=obj_product, weight=weight, noteitem=obj_item, inv=obj_invitem)
            qtyc = obj_invcontrol.inventory
            qtyc = qtyc + qtyz
            obj_invitem.item = qty

            obj_invitem.item = qty
            obj_invitem.save()
            
            obj_invcontrol.inventory = qtyc
            obj_invcontrol.save()
                
    return render(request, 'note/partials/noteitem.html', {'noteitem': obj_item, 'note': note})

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

