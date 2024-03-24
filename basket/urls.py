from django.urls import path
from .views import *

urlpatterns = [
    path('', BasketCreateApiView.as_view(), name='basket-create'),
    path('<str:uuid>/', BasketRetrieveApiView.as_view(), name='basket-detail'),
    path('item/<str:uuid>/', BasketItemCreateApiView.as_view(), name='basket-item-create'),
    path('update-item/<int:id>/', BasketItemUpdateQuantityAPIView.as_view(), name='basket-item-update'),
]