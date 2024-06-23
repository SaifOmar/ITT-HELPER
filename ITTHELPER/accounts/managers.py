from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser,Group,Permission
from django.contrib.auth.models import Permission





class MyUserManager(BaseUserManager):
    def _create_user(self,email,password, username, phone_number,**extra_fields):
        if not email :
            raise ValueError("email must be set")
        if not username :
            raise ValueError("username must be set")
        user = self.model(username=username,email=email,phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,username,phone_number,**extra_fields):
        if not extra_fields.get("last_name"):
            raise ValueError("Last name must be set")
        if not extra_fields.get("first_name"):
            raise ValueError("First Name must be set")
        # if not extra_fields.get("date_of_birth"):
        #     raise ValueError("You must enter your date of birth")
        user = self._create_user(email=email,username=username,password=password,phone_number=phone_number,**extra_fields)
        if extra_fields.get("is_company") == True:
            group = Group.objects.get(name="Company")
            user.groups.add(group)
        else :
            group = Group.objects.get(name="User")
            user.groups.add(group)
        return user
    
    def create_superuser(self,email,password,username,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        user = self._create_user(email=email,password=password,username=username,**extra_fields)
        return user



