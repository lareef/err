import collections
from dataclasses import fields
from django import forms

from util.models import UserProfile
from .models import Product, PurchaseOrder, PurchaseOrderItem
from django.forms.models import (
    modelform_factory,
    modelformset_factory,
    inlineformset_factory    
)

class ProductModelForm(forms.Form):
    class Meta:
        model = Product
        fields = (
            'collection', 'description', 'reorder_level', 
        )

class POForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = (
            'purchase_order_id',
            'supplier',
        )        
class POModelForm(forms.Form):
    class Meta:
        fields = (
            'purchase_order_id', 'supplier',
            'product', 'purchase_order_item_weight', 'purchase_order_item_cost'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Geerate PO id here
        # poId=dict(Client.objects.values_list('clientName', 'id'))
        self.fields['poid'] = forms.CharField(label='Purchase Order Number', required=True)
        self.fields['supplier'] = forms.ModelChoiceField(label='Supplier', queryset=UserProfile.objects.all(), required=True)
        self.fields['product'] = forms.ModelChoiceField(label='Product', queryset=Product.objects.all(), required=True)
        self.fields['purchase_order_item_weight'] = forms.DecimalField(label='Item Weight', required=True)
        self.fields['purchase_order_item_cost'] = forms.DecimalField(label='Item Cost', required=True)

    def clean_fields_(self, *args, **kwargs):
        poid = self.cleaned_data.get('poid')
        supplier= self.cleaned_data.get('supplier')
        product= self.cleaned_data.get('product')
        errProcess = self.cleaned_data.get('errProcess')
        return errProcess

class POItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = (
            'product', 'purchase_order_item_weight', 'purchase_order_item_cost'
        )

POItemsFormSet = inlineformset_factory(
    PurchaseOrder,
    PurchaseOrderItem,
    POItemForm,
    can_delete=False,
    min_num=1,
    extra=0,
)