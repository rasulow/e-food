from rest_framework import serializers
from .models import *
from product.serializers import ProductDetailSerializer



        
        
class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('product', 'quantity',)

class BasketItemProductSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()
    
    class Meta:
        model = BasketItem
        fields = ('id', 'product', 'quantity',)
        
        
class BasketItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('quantity',)
        

class BasketDetailSerializer(serializers.ModelSerializer):
    items = BasketItemProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Basket
        fields = ('id', 'user', 'uuid', 'total_price', 'items',)