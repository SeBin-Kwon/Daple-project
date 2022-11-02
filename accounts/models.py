from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    phone = PhoneNumberField(unique = True, null = False, blank = False, region="KR")
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')