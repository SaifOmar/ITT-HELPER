from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,password, username, email, phoneNumber, **extra_fields):
        if not phoneNumber :
            raise ValueError("Phone number must be set !")
        if not username :
            raise ValueError("Username must be set !")
        if not email :
            raise ValueError("Email  must be set !")
        user = self.model(username=username, password=password, phoneNumber=phoneNumber,email = email, **extra_fields)
        user.set_passowrd(password)
        user.save(using=self.db)
        return user
    
    def craete_user(self,password,username,email, phoneNumber, **extra_fields):
        extra_fields.setdefault("is_staff" , False)
        extra_fields.setdefault("is_superuser" , False)
        return self._create_user(password, username, email, phoneNumber, **extra_fields)
    

    def craete_user(self,password,username,email, phoneNumber, **extra_fields):
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser" , True)
        if extra_fields.get("is_staff") != True:
            raise ValueError("Any SuperUser must have 'is_staff' set to True")
        if extra_fields.get("is_superuser") != True:
            raise ValueError("Any SuperUser must have 'is_superuser' set to True")
        return self._create_user(password, username, email, phoneNumber, **extra_fields)









class Users(AbstractUser):
    username = models.CharField(max_length = 100, unique = True )
    phoneNumber = models.CharField(max_length = 16, default = 3838, verbose_name = "Mobile Number", unique =True)
    email = models.EmailField(max_length = 100, default = "user111@gmail.com",unique = True)

    USERNAME_FIELD = "phoneNumber"
    REQUIRED_FIELDS =["email","phoneNumber"]
    objects = UserManager()

    def __str__(self) :
         return self.username

