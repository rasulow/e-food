from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from .filters import CategorySlugFilterBackend
from django_filters.rest_framework import DjangoFilterBackend



class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryDetailApiView(generics.RetrieveAPIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            pass
        
        try:
            subcategory = SubCategory.objects.get(slug=slug)
            serializer = SubCategorySerializer(subcategory)
            return Response(serializer.data)
        except SubCategory.DoesNotExist:
            pass
        
        try:
            supersubcategory = SuperSubCategory.objects.get(slug=slug)
            serializer = SuperSubCategorySerializer(supersubcategory)
            return Response(serializer.data)
        except SuperSubCategory.DoesNotExist:
            return Response({'message': 'Not found'}, status=404)
    
    
    
    
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug', 'brand__slug']

    def filter_queryset(self, queryset):
        category_slug = self.request.query_params.get('category__slug', None)
        if category_slug:
            queryset = queryset.filter(
                category__slug=category_slug
            ) | queryset.filter(
                subcategory__slug=category_slug
            ) | queryset.filter(
                supersubcategory__slug=category_slug
            )
        return queryset




class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    
    
class BrandListApiView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    