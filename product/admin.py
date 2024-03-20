from django.contrib import admin
from django.utils.html import format_html
from . import models


    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_tm', 'name_ru',)
    
    
@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_tm', 'name_ru', 'category',)
    
    
@admin.register(models.SuperSubCategory)
class SuperSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_tm', 'name_ru', 'category', 'subcategory',)


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo', 'website', 'country',)

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-width:50px; max-height:50px;" />', obj.logo.url)
        else:
            return 'No Logo'
    
    display_logo.allow_tags = True
    display_logo.short_description = 'Logo'
    
    
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'product',)

    def show_image(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="max-width:50px; max-height:50px;" />', obj.img.url)
        else:
            return 'No Logo'
    
    show_image.allow_tags = True
    show_image.short_description = 'Image'
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('rating',)
    list_display = ('name_tm', 'name_ru', 'sku', 'stock_quantity', 'price', 'brand', 'is_original', 'is_new', 'rating',)
    list_filter = ('brand', 'is_original', 'is_new',)
    
    
@admin.register(models.Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('product', 'user',)