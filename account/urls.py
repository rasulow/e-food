from django.urls import path
from .views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    UserRegistrationsView
)

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/register/', UserRegistrationsView.as_view(), name='register'),
]