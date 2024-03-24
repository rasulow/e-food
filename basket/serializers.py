from rest_framework import serializers
from .models import *


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'user', 'uuid', 'total_price',)
        
        
class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('product', 'quantity',)
        
        
class BasketItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('quantity',)