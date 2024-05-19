from django.db import models
from basket.models import Basket

class PaymentType(models.Model):
    type = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'payment_type'
        verbose_name = 'Payment Type'
        verbose_name_plural = 'Payment Types'
    
    def __str__(self) -> str:
        return self.type
    
    
class DeliveryType(models.Model):
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    class Meta:
        db_table = 'delivery_type'
        verbose_name = 'Delivery Type'
        verbose_name_plural = 'Delivery Types'
        
    def __str__(self) -> str:
        return self.type
    
    

class Checkout(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    payment = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    address_detail = models.CharField(max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.ForeignKey(DeliveryType, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=100,
        choices=(
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('delivered', 'Delivered'),
            ('canceled', 'Canceled'),
        ),
        default='confirmed',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'checkout'
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'
        ordering = ['-created_at']
        
        
    def __str__(self) -> str:
        return self.phone_number