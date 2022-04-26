from django.db import models
class ClientType(models.Model):
    client_type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.client_type
    
class Client(models.Model):
    client = models.CharField(max_length=100)
    client_type = models.ManyToManyField(ClientType)
    
    def __str__(self):
        return self.client
    
class Location(models.Model):
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.location
    
class Notekey(models.Model):
    notekey = models.CharField(max_length=10, unique=True, null=False)
    
    def __str__(self):
        return self.notekey

class Notetype(models.Model):
    notetype = models.CharField(max_length=20)

    def __str__(self):
        return self.notetype

class Status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status
        
class Note(models.Model):
    notekey = models.ForeignKey(Notekey, on_delete=models.CASCADE, related_name="%(class)s")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="%(class)s")
    created_on = models.DateTimeField(auto_now_add=True)
    notetype = models.ForeignKey(Notetype, on_delete=models.CASCADE, related_name="%(class)s")
    is_final = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="statuses", default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="locations", default=1)
    
    def __int__(self):
        return self.id

class Noteitemkey(models.Model):
    notekey = models.ForeignKey(Notekey, on_delete=models.CASCADE, related_name='notekeys')
    noteitemkey = models.CharField(max_length=25, null=False)
    
    def __str__(self):
        return self.noteitemkey

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name

class Noteitem(models.Model):
    notekey = models.ForeignKey(Notekey, on_delete=models.CASCADE, related_name="%(class)s")
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="%(class)s")
    noteitemkey = models.ForeignKey(Noteitemkey, on_delete=models.CASCADE, related_name="%(class)s")
    notetypekey = models.ForeignKey(Notetype, on_delete=models.CASCADE, related_name="notetypes")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    is_final = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
      
    def __int__(self):
        return self.noteitemkey
    
class PO(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class POItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class PR(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class PRItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class SO(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class SOItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class SR(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class SRItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class CO(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class COItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class WO(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class WOItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class WI(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class WIItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class WR(Note):
    typ = models.CharField(max_length=10)

    def __int__(self):
        return self.notekey
      
class WRItem(Noteitem):
    typ = models.CharField(max_length=10)
    
    def __int__(self):
        return self.noteitemkey

class Inv(models.Model):
    item = models.IntegerField(default=0)
    product = models.ForeignKey(Product, related_name='%(class)s', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        return self.id
    
class Invitem(models.Model):
    inv = models.ForeignKey(Inv, related_name='%(class)s', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="%(class)s")
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        abstract = True

    def __int__(self):
        return self.id
    
class InvControl(Invitem):
    noteitem = models.ForeignKey(Noteitem, on_delete=models.CASCADE, related_name="%(class)s")
    inventory = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
    
class WorkInvControl(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    inventory = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)