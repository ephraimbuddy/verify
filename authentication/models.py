
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from phone.models import TimestampedModel
import pyotp

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a `User` with an email and password."""
        
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):

        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email,password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default = True)

    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'

    key = models.CharField(max_length=100, unique=True, blank=True)
    
    enable_authenticator = models.BooleanField(default=False) #We can use this to enable 2fa for users
    objects = UserManager()

    class Meta:
        verbose_name ='user'
        verbose_name_plural = 'users'

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

    def get_short_name(self):
        
        return self.first_name
    
    def authenticate(self, otp):
        """ This method authenticates the given otp"""
        provided_otp = 0
        try:
            provided_otp = int(otp)
        except:
            return False
        #Here we are using Time Based OTP. The interval is 60 seconds.
        #otp must be provided within this interval or it's invalid
        t = pyotp.TOTP(self.key, interval=300)
        return t.verify(provided_otp)