from django.contrib import admin
from . import models

class POItemInLineAdmin(admin.TabularInline):
    model = models.PurchaseOrderItem

class POAdmin(admin.ModelAdmin):
    inlines = [POItemInLineAdmin]

admin.site.register(models.PurchaseOrder, POAdmin)
admin.site.register(models.Collection)
admin.site.register(models.Product)