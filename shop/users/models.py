from django.db import models

from django.db import models
from django.contrib.auth.models import PermissionsMixin
# substitute the default Django User model:
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class UserModelManager(BaseUserManager):
    """Allow Django to work with the custom 'UserModel' user model."""

    def create_user(self, email, name, password):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  # this hashes the password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with giver details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Substitute the default Django 'User' model.
    Use the email address for authentication instead of a username.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""
        return f'{self.name} ({self.email})'

    def get_short_name(self):
        """Used to get a user's short name."""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        return self.email

    class Meta:
        verbose_name = 'User'
        ordering = ('name',)

