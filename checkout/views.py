from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class CheckoutTypesAPIView(APIView):
    def get(self, request):
        payment_types = PaymentType.objects.all()
        delivery_types = DeliveryType.objects.all()
        
        payment_serializer = PaymentTypeSerializer(payment_types, many=True)
        delivery_serializer = DeliveryTypeSerializer(delivery_types, many=True)
        
        data = {
            'payment': payment_serializer.data,
            'delivery': delivery_serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    
    
class CheckoutCreateAPIView(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer