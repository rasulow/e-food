from django.urls import path
from .views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    UserRegistrationsView,
    AddressListCreateAPIView
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserRegistrationsView.as_view(), name='register'),
    path('address/', AddressListCreateAPIView.as_view(), name='address'),
]