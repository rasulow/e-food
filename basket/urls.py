from django.urls import path
from .views import *

urlpatterns = [
    path('', BasketCreateApiView.as_view(), name='basket-create'),
    path('<str:uuid>/', BasketRetrieveApiView.as_view(), name='basket-detail')
]