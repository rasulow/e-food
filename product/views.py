from rest_framework import generics
from .models import *
from .serializers import *
from .filters import CategorySlugFilterBackend
from django_filters.rest_framework import DjangoFilterBackend



class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug', 'subcategory__slug', 'supersubcategory__slug']

