from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register',views.RegisterView.as_view(),name="register"),
    path("login_user",views.LoginView.as_view(),name="login_view"),
    path("logout_user",views.LogoutView.as_view(),name="logout_view"),
    path('signup',views.sign_up_user,name="sign_up"),
    path('login',views.login_user,name="login_user"),
    path("logout",views.logout,name="logout_user")
]
