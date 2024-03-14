from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        if request and 'Accept-Language' in request.headers:
            lang = request.headers['Accept-Language']
            if lang.startswith('ru'):
                data['name'] = data.pop('name_ru', None)
                data.pop('name_tm', None)
            elif lang.startswith('tk'):
                data['name'] = data.pop('name_tm', None)
                data.pop('name_ru', None)
        ordered_data = {
            'id': data.get('id'),
            'name': data.get('name'),
            'icon': data.get('icon'),
            'slug': data.get('slug'),
            'created_at': data.get('created_at'),
            'updated_at': data.get('updated_at'),
        }
        return ordered_data