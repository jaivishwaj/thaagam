from django.db import models

# Create your models here.
from django.contrib.auth.models import Group, AbstractUser




class AlphaNumericFieldfive(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 5  # Set fixed max_length for alphanumeric field
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_alphanumeric():
        alphanumeric = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )
        return alphanumeric.upper()


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager


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
            raise ValueError("Superuser must have is_superuser=Trzeue.")

        return self.create_user(email, password, **extra_fields)

from django.contrib.auth.models import AbstractUser
class Staff_UserAuth(AbstractUser):
    objects = CustomUserManager()

    # Fields as per your Firestore structure
    email = models.EmailField(unique=True)  # Add unique constraint to email field
    username = models.CharField(max_length=150, unique=True)
    last_name = None
    referral_code = AlphaNumericFieldfive(unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = AlphaNumericFieldfive.generate_alphanumeric()
            while Staff_UserAuth.objects.filter(
                referral_code=self.referral_code
            ).exists():
                self.referral_code = AlphaNumericFieldfive.generate_alphanumeric()
        super(Staff_UserAuth, self).save(*args, **kwargs)


groups = [
    "Staff",
    "Admin",
    "Superuser",
]


from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import connection



@receiver(post_migrate)
def create_groups(sender, **kwargs):
    with connection.cursor() as cursor:
        table_names = connection.introspection.table_names(cursor)
        if "auth_group" in table_names:
            for group_name in groups:
                Group.objects.get_or_create(name=group_name)
        else:
            print("auth_group table does not exist, skipping group creation.")





