from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup',views.sign_up_user,name="sign_up"),
    path('login',views.login_user,name="login_user"),
    path('register',views.RegisterView.as_view(),name="register"),
]
