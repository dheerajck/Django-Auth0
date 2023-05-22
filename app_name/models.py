from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    email = models.EmailField()  # unique=True, if we are allowing social auth and email + password login, email cant be unique
    uid = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email
