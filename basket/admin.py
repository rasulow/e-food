from django.contrib import admin
from .models import *

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    exclude = ('total_price',)
    list_display = ('id', 'user', 'uuid', 'total_price',)
    
    
@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    exclude = ('total_price',)
    list_display = ('id', 'basket', 'product', 'quantity', 'total_price',)