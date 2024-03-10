from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,default=None,unique=True)
    objects = MyUserManager()

    REQUIRED_FIELDS = ["email","phone_number"]


    def __str__(self):
        return self.username