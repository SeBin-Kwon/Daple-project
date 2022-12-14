from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from stores.models import Store
from stores.models import Thematag
from stores.models import Foodtag
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    rating_choices= (
        (5, "⭐⭐⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (3, "⭐⭐⭐"),
        (2, "⭐⭐"),
        (1, "⭐"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store', null=True, blank=True)
    foodtag_id = models.ForeignKey(Foodtag, on_delete=models.CASCADE,null=True,blank=True)
    thematag_id = models.ForeignKey(Thematag, on_delete=models.CASCADE,null=True,blank=True)
    review_content = models.TextField()
    # review_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_rating = models.IntegerField(max_length=2, choices=rating_choices)
    # review_taste = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # review_price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # review_service = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_taste = models.IntegerField(max_length=2, choices=rating_choices)
    review_price = models.IntegerField(max_length=2, choices=rating_choices)
    review_service = models.IntegerField(max_length=2, choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    review_image = ProcessedImageField(upload_to='images/', blank=True,
    processors=[ResizeToFill(400,300)],
    format='JPEG',
    options={'quality':100})
    like_count = models.IntegerField(default=0)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)