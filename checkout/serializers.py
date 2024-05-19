from rest_framework import serializers
from .models import *
from basket import serializers as basket_serializers


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"
        
        
class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = "__all__"
        

class CheckoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
        
        
class CheckoutListSerializer(serializers.ModelSerializer):
    basket = basket_serializers.BasketDetailSerializer()
    payment = PaymentTypeSerializer()
    delivery = DeliveryTypeSerializer()
    
    class Meta:
        model = Checkout
        fields = ('id', 'basket', 'payment', 'delivery', 'status')
        
    