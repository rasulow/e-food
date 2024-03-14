# filters.py
from rest_framework import filters


class CategorySlugFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category_slug = request.query_params.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset