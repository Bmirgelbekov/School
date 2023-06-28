from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


""" Переопределил Менеджер чтобы не требовал username """
class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, 
                    phone_number, 
                    email=None, 
                    password=None, 
                    **extra_fields):
        
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, 
                         phone_number, 
                         email=None, 
                         password=None, 
                         **extra_fields):
        
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Teacher(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=50)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.phone_number
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

