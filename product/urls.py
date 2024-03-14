from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListApiView.as_view(), name='category-list')
]
