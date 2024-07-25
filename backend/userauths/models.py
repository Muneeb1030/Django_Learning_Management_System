from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    otp = models.IntegerField(blank=True, null=True)
    full_name = models.CharField( max_length=254, null=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_name = self.email.split('@')[0]
        if self.username == "" or self.username == None:
            self.username = email_name
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_name
        return super(User, self).save( *args, **kwargs)    
    
    
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to="user_folder", default='default.jpg', null=True, blank=True)
    full_name = models.CharField( max_length=254, null=True) 
    country = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.user.full_name
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name== None:
            self.full_name = self.user.full_name
        return super(ProfileUser, self).save(*args, **kwargs)
    
    
def create_user_profile_model(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user = instance)
        
def save_user_profile_model(sender, instance, **kwargs):
    instance.profileuser.save()
    
post_save.connect(create_user_profile_model, sender=User)
post_save.connect(save_user_profile_model, sender=User)
    