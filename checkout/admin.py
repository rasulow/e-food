from django.contrib import admin
from . import models

@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'address', 'status')
    
    
@admin.register(models.PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    
    
@admin.register(models.DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price')