from django.urls import path
from .views import *

urlpatterns = [
    path('checkout-types/', CheckoutTypesAPIView.as_view(), name='checkout-types'),
    path('checkout/', CheckoutListCreateAPIView.as_view(), name='checkout'),
    path('checkout/<int:id>/', CheckoutDetailAPIView.as_view(), name='checkout-detail'),
]