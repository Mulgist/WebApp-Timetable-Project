from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError('이메일 주소를 입력하셔야 합니다.')
        user = self.model(
            email=UserManager.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password):
        su = self.create_user(email=email,
                                   user_name=user_name,
                                   password=password,
                                   )
        su.is_admin = True
        su.save(using=self._db)
        return su


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(
        verbose_name='user_id',
        primary_key=True,
        editable=False
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=127,
        unique=True,
    )
    user_name = models.CharField(
        verbose_name='user_name',
        max_length=63,
        blank=False,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.user_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
