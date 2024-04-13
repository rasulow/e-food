from django.urls import path
from .views import *

urlpatterns = [
    path('checkout-types/', CheckoutTypesAPIView.as_view(), name='checkout-types'),
    path('checkout/', CheckoutCreateAPIView.as_view(), name='checkout'),
]