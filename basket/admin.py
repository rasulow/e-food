from django.contrib import admin
from .models import Basket

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    exclude = ('total_price',)
    list_display = ('id', 'user', 'uuid', 'total_price')