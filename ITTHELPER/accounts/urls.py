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
    path("change_password/mobile",views.ChangePasswordView.as_view,name="change_pw_mobile"),
    path("verify_email/mobile",views.VerifyEmailMobile.as_view(),name="verify_email_mobile"),
    path("verify_email/mobile/confirm/<uidb64>/<token>",views.VerifyEmailCheck.as_view(),name="verify_email_mobile_check"),



    path('signup',views.sign_up_user,name="signup"),
    path('login',views.login_user,name="login"),
    path("logout",views.logout_user,name="logout_user"),
    path("verify_email",views.verify_email,name="verify_email"),
    path("verify_email/pending",views.verify_email_pending,name="verify_pending"),
    path("verify_email/confirm/<uidb64>/<token>",views.verify_email_confirm,name="verify_confirm"),
    path("verify_email/complete",views.verify_email_complete,name="verify_complete"),
    path("change_password/site",views.change_password,name="change_pw_site"),
    path("callback",views.callback,name="callback")
]
