from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import authtoken
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionMixin


class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = model.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=Falss)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get full name of user"""
        return self.name

    def get_short_name(self):
        """Get short name"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email
