from django.db import models


class BaseCategory(models.Model):
    name_tm = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category-icons/')
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class Category(BaseCategory):
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
        
        