from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, email, role, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have an email")
        if not role:
            raise ValueError("Users must have a role")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, role='vendor', password=None):
        user = self.create_user(username, email, role, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('vendor', 'Vendor'),
        ('subvendor', 'Subvendor'),
    )

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)  # ✅ email must be unique
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='vendor')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    def __str__(self):
        return self.username
