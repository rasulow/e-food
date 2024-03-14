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
        return localize_data(data, request)


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
            'created_at': data.get('created_at'),
            'updated_at': data.get('updated_at'),
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
            'created_at': data.get('created_at'),
            'updated_at': data.get('updated_at'),
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
            'created_at': data.get('created_at'),
            'updated_at': data.get('updated_at'),
        }
        return ordered_data



class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product 
        fields = '__all__'
