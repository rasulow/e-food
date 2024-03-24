from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import Basket
from utils.token_handle import get_user
from .serializers import *

class BasketCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = get_user(request)
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