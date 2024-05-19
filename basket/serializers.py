from rest_framework import serializers
from .models import *
from product.serializers import ProductDetailSerializer


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = "__all__"

class BasketItemProductSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()
    
    class Meta:
        model = BasketItem
        fields = "__all__"        
        
class BasketItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = "__all__"
        

class BasketDetailSerializer(serializers.ModelSerializer):
    items = BasketItemProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Basket
        fields = "__all__"