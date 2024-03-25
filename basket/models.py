from django.db import models
from django.contrib.auth.models import User
from product.models import Product
import uuid

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'basket'
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return f'{self.uuid}'



class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'basket_item'
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f'{self.product}'
    
    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        basket_price = 0
        basketItems = BasketItem.objects.filter(basket=self.basket)  # Filter by basket object instead of uuid
        for item in basketItems:
            basket_price += item.total_price
        self.basket.total_price = basket_price
        self.basket.save()
        super().save(*args, **kwargs)
        
    
    