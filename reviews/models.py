from djongo import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from stores.models import Store
from stores.models import Thematag
from stores.models import Foodtag
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store', null=True)
    # foodtag_id = models.ForeignKey(Foodtag, on_delete=models.CASCADE,blank=True)
    # thematag_id = models.ForeignKey(Thematag, on_delete=models.CASCADE,blank=True)
    review_content = models.TextField()
    review_rating = models.IntegerField()
    review_taste = models.IntegerField()
    review_price = models.IntegerField()
    review_service = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    review_image = models.ImageField(upload_to='images/', blank=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)