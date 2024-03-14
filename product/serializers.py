from rest_framework import serializers
from .models import *


def localize_data(data, request):
    if request and 'Accept-Language' in request.headers:
        lang = request.headers['Accept-Language']
        if lang.startswith('ru'):
            data['name'] = data.pop('name_ru', None)
            data.pop('name_tm', None)
        elif lang.startswith('tk'):
            data['name'] = data.pop('name_tm', None)
            data.pop('name_ru', None)
    return data


class SuperSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperSubCategory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return localize_data(data, self.context.get('request'))


class SubCategorySerializer(serializers.ModelSerializer):
    supersubcategories = SuperSubCategorySerializer(many=True)

    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return localize_data(data, self.context.get('request'))


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return localize_data(data, self.context.get('request'))
