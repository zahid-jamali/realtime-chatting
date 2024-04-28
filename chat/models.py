from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser):
    name=models.CharField(max_length=100, verbose_name="Complete Name")
    email=models.EmailField(max_length=100, verbose_name="Email Field", unique=True)
    phone=models.IntegerField(verbose_name="Phone Number")

    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name' ,'phone']

    object=CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class chat_rooms(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    url=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class chattings(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Sender")
    room=models.ForeignKey(chat_rooms, on_delete=models.CASCADE, related_name="Room")
    message=models.TextField(max_length=1000, null=True, blank=True)
    atDate=models.DateField(auto_now_add=True)


    



