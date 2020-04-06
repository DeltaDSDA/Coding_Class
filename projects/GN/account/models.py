from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, nickname, password=None, level=0):
        if not email :
            raise ValueError('must have user email')
        user = self.model(
                email = self.normalize_email(email),
                nickname = nickname,
                level = level
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
                email = self.normalize_email(email),
                nickname = nickname,
                password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()
    
    email = models.EmailField(
        max_length=30,
        unique=True,
    )
    nickname = models.CharField(
        max_length=15,
        null=False,
        unique=True
    )
    level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']
    


