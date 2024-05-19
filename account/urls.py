from django.urls import path
from .views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    UserRegistrationsView,
    AddressListCreateAPIView,
    AddressDestroyAPIView,
    UserInfoAPIView
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/', UserInfoAPIView.as_view(), name='user-info'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserRegistrationsView.as_view(), name='register'),
    path('address/', AddressListCreateAPIView.as_view(), name='address'),
    path('address/<int:id>/', AddressDestroyAPIView.as_view(), name='address_delete'),
]