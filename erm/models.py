from django.db import models
from django.contrib.contenttypes.models import  ContentType
from django.contrib.contenttypes.fields import  GenericForeignKey
from util.models import UserProfile, User

class Collection(models.Model):
    collection_id = models.IntegerField(primary_key=True)
    description = models.TextField()
    
    def __str__(self):
        return self.description

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    description = models.TextField()
    reorder_level = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store = models.TextField()
    
class LocationType(models.Model):
    location_type_id = models.CharField(max_length=1, primary_key=True)
    location_type = models.TextField()    

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    location = models.TextField()
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null = True)
    from_source = models.CharField(max_length=10)
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

class PurchaseOrder(models.Model):
    purchase_order_id = models.IntegerField(primary_key=True)
    purchase_order_date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    purchase_order_total_weight = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    purchase_order_total_items = models.IntegerField(default=0)
    purchase_order_cost = models.DecimalField(max_digits=9, default=0, decimal_places=2)

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    purchase_order_item_weight = models.DecimalField(max_digits=5, decimal_places=2)
    purchase_order_item_cost = models.DecimalField(max_digits=9, decimal_places=2)

class CustomerOrder(models.Model):
    customer_order_id = models.IntegerField(primary_key=True)
    customer_order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_order_total_weight = models.DecimalField(max_digits=5, decimal_places=2)
    customer_order_cost = models.DecimalField(max_digits=9, decimal_places=2)

class CustomerOrderItem(models.Model):
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_order_item_weight = models.DecimalField(max_digits=5, decimal_places=2)
    customer_order_item_cost = models.DecimalField(max_digits=9, decimal_places=2)

class CustomerAdvance(models.Model):
    customer_advance_id = models.IntegerField(primary_key=True)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.PROTECT)
    customer_advance_date = models.DateTimeField(auto_now_add=True)
    
class CustomerAdvanceItem(models.Model):
    customer_advance = models.ForeignKey(CustomerAdvance, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer_advance_item_weight = models.DecimalField(max_digits=5, decimal_places=2)
    customer_advance_item_cost = models.DecimalField(max_digits=9, decimal_places=2)
    
class Sales(models.Model):
    sales_id = models.IntegerField(primary_key=True)
    sales_date = models.DateTimeField(auto_now_add=True)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    sales_total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    advance_payment = models.DecimalField(max_digits=9, decimal_places=2)
    balance_payment = models.DecimalField(max_digits=9, decimal_places=2)

class SalesItem(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    sales_item_weight = models.DecimalField(max_digits=5, decimal_places=2)
    sales_item_cost = models.DecimalField(max_digits=9, decimal_places=2)
    
class Address(models.Model):
    adress = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()