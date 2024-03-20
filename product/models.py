from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    name_tm = models.CharField('name TM', max_length=100)
    name_ru = models.CharField('name RU', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
        abstract = True
        
    def __str__(self):
        return self.name_tm


class BaseCategory(BaseModel):
    icon = models.ImageField(upload_to='category-icons/', blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    
    class Meta:
        abstract = True
        
    
    
class Category(BaseCategory):
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
        
class SubCategory(BaseCategory):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        
        
        
class SuperSubCategory(BaseCategory):
    category = models.ForeignKey(Category, related_name='supersubcategories', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='supersubcategories', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'supersubcategory'
        verbose_name = 'Supersubcategory'
        verbose_name_plural = 'Supersubcategories'
        


class Brand(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField(max_length=50, unique=True, default='brand-slug')
    logo = models.ImageField('LOGO', upload_to='brand-logo/', blank=True, null=True)
    website = models.CharField('Web Site', max_length=50, blank=True, null=True)
    country = models.CharField('Country', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
        verbose_name_plural='Brands'
        
    def __str__(self) -> str:
        return self.name
        
        
class Product(BaseModel):
    sku = models.CharField(
        'SKU',
        max_length=3, 
        choices=(
            ('kg', 'kg'),
            ('pcs', 'pcs'),
        ),
        default='kg',
        help_text = 'Stock keeping unit'
    )
    upc = models.CharField(
        'UPC',
        max_length=50,
        help_text = 'Universal Product Code'
    )
    slug = models.SlugField(max_length=50, unique=True, default='product-slug')
    stock_quantity = models.FloatField(blank=True, null=True)
    description_tm = models.TextField('description TM', blank=True, null=True)
    description_ru = models.TextField('description RU', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    supersubcategory = models.ForeignKey(SuperSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_percent = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_original = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, blank=True, null=True)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'    
        verbose_name_plural = 'Products'    
        ordering = ('-created_at',)



class Image(models.Model):
    img = models.ImageField(upload_to='product-images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['-created_at']
        
        
        
class Favourite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'favourite'
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'
        ordering = ['-created_at']
