from rest_framework import serializers
from .models import *


def localize_data(data, request):
    if request and 'Accept-Language' in request.headers:
        lang = request.headers['Accept-Language']
        if lang.startswith('ru'):
            data['name'] = data.pop('name_ru', None)
            data['description'] = data.pop('description_ru', None)
            data.pop('name_tm', None)
            data.pop('description_tm', None)
        elif lang.startswith('tk'):
            data['name'] = data.pop('name_tm', None)
            data['description'] = data.pop('description_tm', None)
            data.pop('name_ru', None)
            data.pop('description_ru', None)
    return data


class BaseSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        localized_data = localize_data(data, request)

        return localized_data


class SuperSubCategorySerializer(BaseSerializer):
    class Meta:
        model = SuperSubCategory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ordered_data = {
            'id': data.get('id'),
            'name': data.get('name'),
            'icon': data.get('icon'),
            'slug': data.get('slug'),
        }
        return ordered_data


class SubCategorySerializer(BaseSerializer):
    supersubcategories = SuperSubCategorySerializer(many=True)

    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ordered_data = {
            'id': data.get('id'),
            'name': data.get('name'),
            'icon': data.get('icon'),
            'slug': data.get('slug'),
            'children': data.get('supersubcategories'),
        }
        return ordered_data


class CategorySerializer(BaseSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ordered_data = {
            'id': data.get('id'),
            'name': data.get('name'),
            'icon': data.get('icon'),
            'slug': data.get('slug'),
            'children': data.get('subcategories'),
        }
        return ordered_data


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug', 'logo', 'website', 'country',)
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'img',)
        


class ProductListSerializer(BaseSerializer):
    category_slug = serializers.SlugField(source='category.slug', read_only=True)
    subcategory_slug = serializers.SlugField(source='subcategory.slug', read_only=True)
    supersubcategory_slug = serializers.SlugField(source='supersubcategory.slug', read_only=True)
    brand = BrandSerializer()
    thumbnail = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Product 
        fields = (
            'id', 'name_tm', 'name_ru', 'sku', 'upc', 'slug', 'stock_quantity', 'description_tm', 
            'description_ru', 'brand', 'thumbnail', 'price', 'discount_percent', 'is_public', 'is_featured', 
            'is_original', 'is_new', 'rating', 'category_slug', 'subcategory_slug', 'supersubcategory_slug'
        )
        
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.images.exists():
            first_image = obj.images.first()
            if first_image:
                return request.build_absolute_uri(first_image.img.url)
        return None
        
        
class ProductDetailSerializer(BaseSerializer):
    category_slug = serializers.SlugField(source='category.slug', read_only=True)
    subcategory_slug = serializers.SlugField(source='subcategory.slug', read_only=True)
    supersubcategory_slug = serializers.SlugField(source='supersubcategory.slug', read_only=True)
    brand = BrandSerializer()
    images = ImageSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Product 
        fields = (
            'id', 'name_tm', 'name_ru', 'sku', 'upc', 'slug', 'stock_quantity', 'description_tm', 
            'description_ru', 'brand', 'images', 'price', 'discount_percent', 'is_public', 'is_featured', 
            'is_original', 'is_new', 'rating', 'category_slug', 'subcategory_slug', 'supersubcategory_slug'
        )
