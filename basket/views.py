from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import Basket
from utils.token_handle import get_user
from .serializers import *
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class BasketCreateApiView(APIView):
    queryset = Basket.objects.all()  # Define the queryset here

    def post(self, request, *args, **kwargs):
        # user = get_user(request)
        user = None
        basket = Basket.objects.create(user=user)
        return Response(
            {
                'user': user.username if user else None,
                'uuid': basket.uuid
            }, 
            status=status.HTTP_201_CREATED
        )
        
        
class BasketRetrieveApiView(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketDetailSerializer
    lookup_field = 'uuid'
    
    
class BasketItemCreateApiView(generics.CreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    lookup_field = 'uuid'
    
    def post(self, request, *args, **kwargs):
        try:
            basket_uuid = self.kwargs.get('uuid')
            basket = Basket.objects.get(uuid=basket_uuid)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(basket=basket)
            return Response(serializer.data, status=201)
        except Basket.DoesNotExist:
            return Response({"message": "Basket not found"}, status=404)  
        
        
class BasketItemUpdateQuantityAPIView(generics.UpdateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemUpdateSerializer
    lookup_field = 'id'  # Use 'id' or any other field you prefer for lookup

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {'quantity': request.data.get('quantity')}  # Assuming the request data contains only the new quantity

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class BasketItemDeleteApiView(generics.DestroyAPIView):
    queryset = BasketItem.objects.all()
    lookup_field = 'id'    
    