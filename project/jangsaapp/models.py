from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Cat(models.Model):
    name = models.CharField(max_length =200)
    image = models.ImageField(upload_to = 'cat')
    age = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
            return self.name 
    

class Dog(models.Model): 
    image= models.ImageField(upload_to = 'dog')
    name = models.CharField(max_length =200)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now=True) 
    description = models.TextField()

    def __str__(self):
        return self.name 

class Manager(BaseUserManager): 
    def create_user(self,fullname,username, phone_number,email, password=None):
        if not username:
            raise ValueError("Enter a unique username")
        if not fullname:
            raise ValueError("Enter your full name")  
        if not phone_number:
            raise ValueError("You must provide a valid phone number")
        if not email:
            raise ValueError("Provide a valid email address")
        
        user = self.model(
               fullname = fullname,
               username = username,
               phone_number = phone_number,
               email = self.normalize_email(email),
               
        )
        user = set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,password):
        user = self.create_user(  
            username = username, 
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 


class JangsaUser(AbstractBaseUser):
    fullname       = models.CharField(max_length = 50)
    username       = models.CharField(max_length =50, unique=True)
    phone_number   = models.IntegerField()
    email          = models.EmailField(unique=True)
    password       = models.CharField(max_length= 50)
    is_admin       = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True) 
    is_staff       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['password','fullname','email','phone_number'] 

    objects = Manager()
    

    def __str__(self):
        return self.email  
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_Label):
        return True 





# Create your models here.
