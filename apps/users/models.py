from django.db import models
from django.conf import settings
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser

from apps.utils.models import Timestamps


class UserManager(BaseUserManager):
    """
    You can also read about 'user customization' in the docs here
    https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
    """

    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("Phone number is required argument.")
        
        user = self.model(
			phone=self.normalize_phone_number(phone=phone)
		)
        user.set_password(password)
        return user
    
    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email,
        phone and password.
        """
        user = self.create_user(
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
    @classmethod
    def normalize_phone_number(cls, phone: str) -> str:
        """
        Checks if the phone number is a string.
        """
        if not isinstance(phone, str):
            raise ValueError(f"{type(phone)} != str.")
        
        if not phone.rsplit("+")[-1].isdigit():
            raise ValueError("Invalid phone number.")
        return phone.strip()        


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=155, null=True, blank=True
    )
    phone = models.CharField(
        max_length=50, unique=True
    )
    email = models.EmailField(
        null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

class Client(Timestamps):
    user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE
	)
    
    def __str__(self) -> str:
        return f"User_{self.user.id}: {self.user.phone}"