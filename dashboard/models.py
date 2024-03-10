from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)



  
# class Staff_UserAuth(AbstractUser):
#     objects = CustomUserManager()
    
#     username = None
#     last_name = None
    
#     # Fields as per your Firestore structure
#     email = models.EmailField(_("email address"), unique=True)
#     mobile_number = models.CharField(max_length=15, null=True, blank=True)
#     USERNAME_FIELD = "email"
    
#     REQUIRED_FIELDS = []
    

class Staff_UserAuth(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)  # Add this line
    email = models.EmailField(_("email address"), unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



groups = [
    'Staff',
    'Superuser'
]

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import models, connection

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    with connection.cursor() as cursor:
        table_names = connection.introspection.table_names(cursor)
        if "auth_group" in table_names:
            for group_name in groups:
                Group.objects.get_or_create(name=group_name)
        else:
            print("auth_group table does not exist, skipping group creation.")
