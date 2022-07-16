from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from erm.models import Collection, PurchaseOrder, PurchaseOrderItem
from note.models import Product, Cost, Note, Noteitem, Notetype, Client, Location
from util.models import UserProfile
from django.db.models import Q, Count, Sum
from .forms import POItemsFormSet, ProductModelForm, CostModelForm, POItemForm, POForm, POModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

def notelist(request):
    notetypes = Notetype.objects.all()
    clients = Client.objects.all()
    locations = Location.objects.all()
    notes = None
    return render(request, 'erm/note_list.html', {'notes': notes, 'notetypes': notetypes, 'locations': locations, 'clients': clients })


def notelistrep(request):

    notes = None
    
    notetype = request.POST.get('notetype', '')
    client = request.POST.get('client', '')
    location = request.POST.get('location', '')

    my_dict = {'notetype': notetype, 'client': client, 'location': location}  # Your dict with fields
    or_condition = Q()
    for key, value in my_dict.items():
        if value:
            or_condition.add(Q(**{key: value}), Q.AND)

    query_set = Note.objects.filter(or_condition).annotate(p=Sum('noteitem__pcost'), w=Sum('noteitem__weight'))
    #QAr.objects.all().annotate(Count('qaerrors__dept')).filter(dept=1)
    return render(request, 'erm/notelist_data.html', {'notes': query_set})

def noteitemslist(request, pk):
    note = Note.objects.get(id=pk)
    noteitems = Noteitem.objects.filter(note_id=note.id)

    return render(request, 'erm/partials/noteitems_list_rep.html', {'note': note, 'noteitems': noteitems})

def noteitemslist_delete(request, pk):
    return HttpResponse()

class CostCreateView(LoginRequiredMixin, CreateView):
    template_name = "erm/cost_create.html"
    form_class = CostModelForm

    def get_success_url(self):
        return reverse("erm:cost-list") 

class CostListView(LoginRequiredMixin, ListView):
    template_name = "erm/cost_list.html"
    queryset = Cost.objects.all()

class CostDetailView(LoginRequiredMixin, DetailView):
    template_name = "erm/cost_detail.html"
    queryset = Cost.objects.all()
    form_class = CostModelForm

class CostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "erm/cost_update.html"
    queryset = Cost.objects.all()
    form_class = CostModelForm

    def get_success_url(self):
        return reverse("erm:cost-list") 

class CostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "erm/cost_delete.html"
    queryset = Cost.objects.all()

    def get_success_url(self):
        return reverse("erm:cost-list")

class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "erm/product_create.html"
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse("erm:product-list") 

class ProductListView(LoginRequiredMixin, ListView):
    template_name = "erm/product_list.html"
    queryset = Product.objects.all()

class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "erm/product_detail.html"
    queryset = Product.objects.all()
    form_class = ProductModelForm

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "erm/product_update.html"
    queryset = Product.objects.all()
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse("erm:product-list") 

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "erm/product_delete.html"
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("erm:product-list")

''' class POCreateView(LoginRequiredMixin, CreateView):
    template_name = "erm/po_create.html"
    form_class = POForm

    def get_success_url(self):
        return reverse("erm:detail-poitem")
    
def poc(request):
    print(request.POST)
    form = POForm()
    if request.method == "POST":
        form = POForm(request.POST)
        if form.is_valid():
            poid  = form.cleaned_data['purchase_order_id']
            supplier = form.cleaned_data['supplier']
            obj_supplier = UserProfile.objects.get(user_id=supplier.id)
            PurchaseOrder.objects.get_or_create(
                purchase_order_id=poid,
                supplier=obj_supplier,
                # purchase_order_total_weight=purchase_order_item_weight,
                # purchase_order_total_items=1,
                # purchase_order_cost=purchase_order_item_cost,
            )
            return redirect("erm:create-poitem", pk=poid)
    context = {
        "form": form
    }
    return render(request, "erm/po_create.html", context)

class POListView(LoginRequiredMixin, ListView):
    template_name = "erm/doc-list.html"
    queryset = PurchaseOrder.objects.all()

  
def POCreate(request):
    print(request.POST)
    form = POModelForm()
    if request.method == 'POST':
        form = POModelForm(request.POST)
        if form.is_valid():
            poid = form.cleaned_data['poid']
            supplier = form.cleaned_data['supplier']
            product = form.cleaned_data['product']
            purchase_order_item_weight = form.cleaned_data['purchase_order_item_weight']
            purchase_order_item_cost = form.cleaned_data['purchase_order_item_cost']
            # obj_supplier = UserProfile.objects.get(id=supplier.id)
            obj_supplier = UserProfile.objects.get(user_id=supplier.id)
            obj_po, po_create = PurchaseOrder.objects.get_or_create(
                purchase_order_id=poid,
                supplier=obj_supplier,
                purchase_order_total_weight=purchase_order_item_weight,
                purchase_order_total_items=1,
                purchase_order_cost=purchase_order_item_cost,
            )
            
            obj_product = Product.objects.get(product_id=product.product_id)
            PurchaseOrderItem.objects.create(
                purchase_order=obj_po,
                product=obj_product,
                purchase_order_item_weight=purchase_order_item_weight,
                purchase_order_item_cost=purchase_order_item_cost,
            )
            return redirect("erm:create-poitem", pk=poid)
    context = {
        "form": form
    }
    return render(request, "erm/po_head.html", context)
 '''
# class POCreateView(LoginRequiredMixin, CreateView):
#     template_name = "erm/po_create.html"
#     form_class = POForm

#     def get_success_url(self):
#         return reverse("erm:product-list") 

# def create_po(request):
#     form = POModelForm(request.POST or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             po = form.save(commit=False)
#             po.purchase_order = po
#             po.save()
#             return redirect("erm:detail-poitem", pk=po.id)
    
#     context = {
#         "form": form,
#     }
    
#     return render(request, "erm/create_po.html", context)

''' def create_poitem(request, pk):
    po = PurchaseOrder.objects.get(purchase_order_id=pk)
    poitems = PurchaseOrderItem.objects.filter(purchase_order=po)
    form = POItemForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            poitem = form.save(commit=False)
            poitem.purchase_order = po
            poitem.save()
            return redirect("erm:detail-poitem", pk=poitem.id)
        else:
            return render(request, "erm/partials/poitem_form.html", {"form": form})
    
    context = {
        "form": form,
        "po": po,
        "poitem": poitems
    }
    
    return render(request, "erm/create_poitem.html", context)

def create_poitem_form(request):
    print("create_poitem_form" , request.POST)
    context = {
        "form": POItemForm()
    }
    return render(request, "erm/partials/poitem_form.html", context)

def detail_poitem(request, pk):
    print("detail_poitem", request)
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    context = {
        "poitem": poitem
        }
    return render(request, "erm/partials/poitem_detail.html", context)

def delete_poitem(request, pk):
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    poitem.delete()
    #return HttpResponse('')
    return render(request, "erm/create_poitem.html", context)

def update_poitem(request, pk):
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    form = POItemForm(request.POST or None, instance=poitem)
    
    if request.method == "POST":
        if form.is_valid():
            poitem.save()
            return redirect("erm:detail-poitem", pk=poitem.id)
    
    context = {
        "form": form,
        "poitem": poitem
    }
    return render(request, "erm/partials/poitem_form.html", context)

class DocListView(LoginRequiredMixin, ListView):
    template_name = "erm/doc-list.html"
    queryset = PurchaseOrder.objects.all()
    
def create_docitem_form(request):
    print("create_docitem_form" , request.POST)
    context = {
        "form": POItemForm()
    }
    return render(request, "erm/partials/docitem_form.html", context)
    
def detail_docitem(request, pk):
    print("detail_docitem", request)
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    context = {
        "poitem": poitem
        }
    return render(request, "erm/partials/docitem_detail.html", context)

def delete_docitem(request, pk):
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    poitem.delete()
    #return HttpResponse('')
    #return render(request, "erm/create_docitem.html", context)
    return redirect("erm:list-docitem", pk=poitem.purchase_order_id)


def update_docitem(request, pk):
    poitem = PurchaseOrderItem.objects.get(pk=pk)
    form = POItemForm(request.POST or None, instance=poitem)
    
    if request.method == "POST":
        if form.is_valid():
            poitem.save()
            print("poitem", poitem.purchase_order_id, poitem.id)
            #return redirect("erm:detail-docitem", pk=poitem.id)
            #return redirect("erm:docitem-create", pk=poitem.purchase_order_id)
            return redirect("erm:list-docitem", pk=poitem.purchase_order_id)
    
    context = {
        "form": form,
        "poitem": poitem
    }
    return render(request, "erm/partials/docitem_form.html", context)

def docitem_list(request, pk):
    po = PurchaseOrder.objects.get(purchase_order_id=pk)
    poitems = PurchaseOrderItem.objects.filter(purchase_order=po)
    return render(request, "erm/partials/docitem_list.html", {"poitems":poitems})

def docitem_create(request, pk):
    po = PurchaseOrder.objects.get(purchase_order_id=pk)
    poitems = PurchaseOrderItem.objects.filter(purchase_order=po)
    form = POItemForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            poitem = form.save(commit=False)
            poitem.purchase_order = po
            poitem.save()
            #return redirect("erm:detail-docitem", pk=poitem.id)
            return redirect("erm:list-docitem", pk=poitem.purchase_order_id)
        else:
            return render(request, "erm/partials/docitem_form.html", {"form": form})
    
    context = {
        "form": form,
        "po": po,
        "poitem": poitems
    }
    
    return render(request, "erm/docitem_create.html", context)

def doc_create(request):
    print(request.POST)
    form = POForm()
    if request.method == "POST":
        form = POForm(request.POST)
        if form.is_valid():
            poid  = form.cleaned_data['purchase_order_id']
            supplier = form.cleaned_data['supplier']
            obj_supplier = UserProfile.objects.get(user_id=supplier.id)
            PurchaseOrder.objects.get_or_create(
                purchase_order_id=poid,
                supplier=obj_supplier,
            )
            return redirect("erm:docitem-create", pk=poid)
    context = {
        "form": form
    }
    return render(request, "erm/doc_create.html", context) '''