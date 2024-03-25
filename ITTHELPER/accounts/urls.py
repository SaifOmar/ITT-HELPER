from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('register',views.RegisterView.as_view(),name="register"),
    path('login_user', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("logout_user",views.LogoutView.as_view(),name="logout_view"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),



    path('signup',views.sign_up_user,name="sign_up"),
    path('login',views.login_user,name="login_user"),
    path("logout",views.logout_user,name="logout_user"),
]
