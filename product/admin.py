from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.SuperSubCategory)
admin.site.register(models.Brand)
admin.site.register(models.Image)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('rating',)