from django.contrib.auth.backends import BaseBackend
from .models import CustomUser
from django.db.models import Q

class MyCustomBackend(BaseBackend):
    def authenticate(self,request,password=None,u_e_p=None):
        try:
             user = CustomUser.objects.get(
                  Q(email=u_e_p) | Q(username=u_e_p) | Q(phone_number=u_e_p)
             )
             pwd_valid=user.check_password(password)
             if pwd_valid:
                 return user
             return None
        except CustomUser.DoesNotExist:
             return None


    def get_user(self,user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None