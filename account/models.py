from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50, default="")
