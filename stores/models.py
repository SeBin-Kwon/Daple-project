from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


# Create your models here.
class Thematag(models.Model):
    thematag_name = models.CharField(max_length=20)


class Foodtag(models.Model):
    foodtag_name = models.CharField(max_length=20)


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_grade = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    store_tel = models.CharField(max_length=100)
    store_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_stores')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    store_x = models.CharField(default=0,max_length=100)
    store_y = models.CharField(default=0,max_length=100)
    store_url = models.CharField(max_length=100)
    kakao_id= models.IntegerField(blank=True)
    # review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE, related_name='store_reviews', blank=True, null=True)
    store_image = models.URLField(blank=True)
    # ProcessedImageField(
    #     upload_to="stores/",
    #     blank=True,
    #     processors=[ResizeToFill(900, 1200)],
    #     format="JPEG",
    #     options={"quality": 90},
    # )
    foodtag_id = models.ForeignKey(Foodtag, on_delete=models.CASCADE,null=True,blank=True)
    thematag_id = models.ForeignKey(Thematag, on_delete=models.CASCADE,null=True,blank=True)
