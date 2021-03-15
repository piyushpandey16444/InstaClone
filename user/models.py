from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class User(AbstractUser):
    display_picture = models.ImageField(upload_to='dpImages')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = BaseException()
