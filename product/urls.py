from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListApiView.as_view(), name='category-list'),
    path('product/', views.ProductListApiView.as_view(), name='product-list'),
    path('product/<slug:slug>/', views.ProductDetailApiView.as_view(), name='product-detail'),
    path('brand/', views.BrandListApiView.as_view(), name='brand-list'),
]
