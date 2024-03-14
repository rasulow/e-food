from django.db import models


class BaseCategory(models.Model):
    name_tm = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category-icons/', blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name_tm
    
    
    
class Category(BaseCategory):
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
        
        
        
class SubCategory(BaseCategory):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        ordering = ['-created_at']
        
        
        
class SuperSubCategory(BaseCategory):
    category = models.ForeignKey(Category, related_name='supersubcategories', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='supersubcategories', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'supersubcategory'
        verbose_name = 'Supersubcategory'
        verbose_name_plural = 'Supersubcategories'
        ordering = ['-created_at']