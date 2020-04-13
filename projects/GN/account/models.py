from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    num = models.AutoField(primary_key = True)

