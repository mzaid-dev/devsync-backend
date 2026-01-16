from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin , BaseUserManager
from django.utils import timezone
import random
from datetime import timedelta
import secrets


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password=None,role='user'):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=True):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            role='admin'
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50,unique=True)
    role = models.CharField(max_length=20,choices=[('admin','Admin'),('user','User')],default='user')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} ({self.email})'
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class EmailOTP(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='otps')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not self.otp:
            val = secrets.randbelow(900000) + 100000
            self.otp = str(val)
        
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args,**kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at