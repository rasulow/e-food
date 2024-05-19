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
    
    
    
class CheckoutListCreateAPIView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CheckoutCreateSerializer
        elif self.request.method == 'GET':
            return CheckoutListSerializer
        
        
class CheckoutDetailAPIView(generics.RetrieveAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutListSerializer
    lookup_field = 'id'