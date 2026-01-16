from django.urls import path
from apps.accounts.views import (
    SignupAPIView,
    LoginAPIView,
    VerifyOTPAPIView,
    ProfileAPIView,
    LogoutAPIView,
    UserListAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('verify-otp/',VerifyOTPAPIView.as_view(),name='verify-otp'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/',ProfileAPIView.as_view(),name='profile'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]