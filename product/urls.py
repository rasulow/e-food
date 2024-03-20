from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListApiView.as_view(), name='category-list'),
    path('category/<slug:slug>/', views.CategoryDetailApiView.as_view(), name='category-detail'),
    path('product/', views.ProductListApiView.as_view(), name='product-list'),
    path('product/<slug:slug>/', views.ProductDetailApiView.as_view(), name='product-detail'),
    path('brand/', views.BrandListApiView.as_view(), name='brand-list'),
    path('favourite/', views.FavouriteView.as_view(), name='favourite'),
]
