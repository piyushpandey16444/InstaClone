from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .managers import CustomUserManager


class User(AbstractUser):
    display_picture = models.ImageField(
        upload_to='dpImages', null=True, blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]

    objects = CustomUserManager()
