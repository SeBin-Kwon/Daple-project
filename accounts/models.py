from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    phone = PhoneNumberField(null = False, blank = True, region="KR")
    nickname = models.CharField(max_length=50)
    Is_owner = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', default=0)