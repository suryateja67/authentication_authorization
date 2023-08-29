
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,Group,Permission,BaseUserManager


class CustomUser(AbstractUser,PermissionsMixin):
    roles = [
        ('Client', 'Client'),
        ('Admin', 'Admin'),
    ]
    

    role = models.CharField(choices=roles, max_length=6,default="Client")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email','role')
    def __str__(self):
        return "{}".format(self.username)
