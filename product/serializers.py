from rest_framework import serializers
from .models import AbstractCategory

class ChildCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractCategory
        fields = ['name_tm', 'name_ru', 'icon']

class AbstractCategorySerializer(serializers.ModelSerializer):
    child_categories = ChildCategorySerializer(many=True, read_only=True)

    class Meta:
        model = AbstractCategory
        fields = ['name_tm', 'name_ru', 'icon', 'child_categories']

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
        # Reorder the keys to show 'name' first, followed by 'icon'
        ordered_data = {
            'name': data.get('name'),
            'icon': data.get('icon'),
            'child_categories': data.get('child_categories')
        }
        return ordered_data
