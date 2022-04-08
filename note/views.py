from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Client, Note, Noteitem, Notekey, Notetype, Status, Noteitemkey, PO, POItem, Product, SO, SOItem, CO, COItem, WO, WOItem, Inv, InvControl

def notes(request):
    notetypes = Notetype.objects.all()
    clients = Client.objects.all()
    #pk = request.POST.get('notetype', '')
    selected = {}
    notes = None
    client = None
    s_notetype = None
    if request.method == 'GET':
        s_notetype = request.GET.get('notetype', '')
        client = request.GET.get('client', '')

        selected['client']=client
        selected['notetype']=s_notetype
    
        if s_notetype or client:
            if s_notetype and client:
                notes = Note.objects.filter(notetype_id=s_notetype, client_id=client)
            if s_notetype and client=="":
                notes = Note.objects.filter(notetype_id=s_notetype)
            if s_notetype=="" and client:
                notes = Note.objects.filter(client_id=client)
        return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients, 's_notetype': s_notetype})
    return render(request, 'note/init.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients, 's_notetype': s_notetype, 'selected': selected})

# def notes_client(request):
#     notetypes = Notetype.objects.all()
#     #pk = request.POST.get('notetype', '')
#     notes = None
#     client = None
#     if request.method == 'GET':
#         notetype = request.GET.get('notetype', '')
#         client = request.GET.get('client', '')
#         if notetype and client:
#             notes = Note.objects.filter(notetype_id=notetype, client=client)
#         return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes, 'client': client})
#     return render(request, 'note/init.html', {'notes': notes, 'notetypes': notetypes, 'client': client})

def init(request):
    notetypes = Notetype.objects.all()
    clients = Client.objects.all()
    #pk = request.POST.get('notetype', '')
    notes = None
    return render(request, 'note/init.html', {'notes': notes, 'notetypes': notetypes, 'clients': clients})

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

        if obj_notetype.id == 2:
            obj_so, create_so = SO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_so.note_ptr_id)

        if obj_notetype.id == 3:
            obj_co, create_po = CO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_co.note_ptr_id)

        if obj_notetype.id == 4:
            obj_wo, create_so = WO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id, client=obj_client)
            obj_note = Note.objects.get(id=obj_wo.note_ptr_id)
        
        #obj_notekey, create_notekey = Notekey.objects.get_or_update(notekey=obj_notekey, notetype=obj_notetype)

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
    products = Product.objects.all()
    noteref = note.notekey_id
    noteitems = Noteitem.objects.filter(notekey_id=noteref, notetypekey_id=note.notetype_id)
    #note = Note.objects.filter(notekey_id=notekey)[:1].get()

    return render(request, 'note/noteitems.html', {'noteref': noteref, 'noteitems': noteitems, 'note': note, 'products': products})

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
    product = request.POST.get('product', '')
    quantity = request.POST.get('quantity', '')
    cost = request.POST.get('cost', '')
    weight = request.POST.get('weight', '')

    if note:
        note = Note.objects.get(id=note)
        obj_notekey = Notekey.objects.get(id=note.notekey_id)
        obj_notetype = Notetype.objects.get(id=note.notetype_id)
        obj_noteitemkey, create_noteitemkey = Noteitemkey.objects.get_or_create(notekey=obj_notekey)
        if product:
            obj_product = Product.objects.get(product_name=product)
            #obj_invitem, create_invitem = Invitem.objects.get_or_create(product=obj_product, weight=weight)
            
            if note.notetype_id == 1:
                obj_item, create_poitem = POItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    notetypekey=obj_notetype,
                    product=obj_product,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)
            if note.notetype_id == 2:
                obj_item, create_poitem = SOItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    product=obj_product,
                    notetypekey=obj_notetype,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)
            if note.notetype_id == 3:
                obj_item, create_poitem = COItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    notetypekey=obj_notetype,
                    product=obj_product,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)
            if note.notetype_id == 4:
                obj_item, create_poitem = WOItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    product=obj_product,
                    notetypekey=obj_notetype,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)

            obj_invitem, create_invitem = Inv.objects.get_or_create(product=obj_product, weight=weight)   
            obj_invcontrol = InvControl.objects.get_or_create(inv_id=obj_invitem.id, noteitem=obj_item,
                                                              product=obj_product, weight=weight)
                               
            #noteitem = Noteitem.objects.get(id=obj_poitem.noteitem_ptr_id)
    
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

