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

