from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryDetailApiView(generics.RetrieveAPIView):
    queryset = Category.objects.none()

    def get_object(self):
        slug = self.kwargs.get('slug')
        queryset = Category.objects.filter(slug=slug)
        if queryset.exists():
            return queryset.first()

        queryset = SubCategory.objects.filter(slug=slug)
        if queryset.exists():
            return queryset.first()

        queryset = SuperSubCategory.objects.filter(slug=slug)
        if queryset.exists():
            return queryset.first()

        return None

    def get_serializer_class(self):
        instance = self.get_object()
        if instance:
            if isinstance(instance, Category):
                return CategorySerializer
            elif isinstance(instance, SubCategory):
                return SubCategorySerializer
            elif isinstance(instance, SuperSubCategory):
                return SuperSubCategorySerializer
        return None

    def get(self, request, slug):
        instance = self.get_object()
        serializer_class = self.get_serializer_class()

        if instance and serializer_class:
            serializer = serializer_class(instance, context={'request': request})
            return Response(serializer.data)
        else:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
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
    
    
class FavouriteView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Product.objects.filter(favourite__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        elif self.request.method == 'POST':
            return FavouriteCreateSerializer

    def post(self, request, *args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]

        product_id = request.data.get('product')
        if Favourite.objects.filter(product_id=product_id, user=request.user).exists():
            return Response({'message': 'Product already in favorites'}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
