from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
import os

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


def getProfileImagePath(instance, filename):
    if instance.id is not None:
        return os.path.join("uploads/profile/profile_id_%d" % instance.id, filename)
    else:
        return os.path.join("uploads/profile/profile", filename)


# Custom UserApi manager
class MyUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.user_role_id = 1
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Admin role_id = 1
    Staff role_id = 2
    Vendors role_id = 3
    Clients role_id = 4
    """
    user_role_id = models.IntegerField(db_index=True, default=0, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(db_index=True, max_length=128, unique=True, blank=True, null=True)
    email = models.EmailField(db_index=True, max_length=128, unique=True)
    mobile_number = models.CharField(db_index=True, max_length=20, blank=True, null=True)

    password = models.CharField(max_length=128, blank=True, null=True)
    confirm_password = models.CharField(max_length=128, blank=True, null=True)
    forgot_password_string = models.CharField(max_length=128, blank=True, null=True)

    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to=getProfileImagePath, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def has_perm(self, perm, obj=None):
        """Does the UserApi have a specific permission?"""
        # Simplest possible answer: Yes, always
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Does the UserApi have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'auth_user'
