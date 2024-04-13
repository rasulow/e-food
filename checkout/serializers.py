from rest_framework import serializers
from .models import *


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id', 'type',)
        
        
class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('id', 'type', 'price')
        

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('id', 'basket', 'payment', 'full_name', 'phone_number', 'address', 'address_detail', 'note', 'delivery') 