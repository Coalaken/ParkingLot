from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser


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
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
        