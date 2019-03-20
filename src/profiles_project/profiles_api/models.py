from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class UserProfileManager(BaseUserManager):
    """help django to work with ower costume user model"""

    def creat_user(self,email,name,password=None):
        """creation a new user profile object."""
        if not email:
            raise ValueError('users must have an email adress.')
        
        email= self.normalize_email(email)
        user =self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """create and save a new superuser with given detail"""

        user = self.creat_user(email,name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user




# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user Profile" inside our system """
    email = models.EmailField( max_length=254, unique=True)
    name= models.CharField( max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    object = UserProfileManager ()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['name']

    def get_full_name(self) :
        """used to get the users full name """

        return self.name
    

    def get_short_name(self):
        """ used to get the users short name """

        return self.name

    def __str__(self):
        """ django used this whe we want to convert the object to string """
        return self.email

    
    
    

    pass