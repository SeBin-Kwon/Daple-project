from djongo import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_grade = models.IntegerField()
    store_tel = models.IntegerField()
    store_liked = models.IntegerField(default=0)
    store_image = models.ImageField(upload_to='stores')
    store_x = models.IntegerField(default=0)
    store_y = models.IntegerField(default=0)
    image = ProcessedImageField(
        upload_to="stores/",
        blank=True,
        processors=[ResizeToFill(900, 1200)],
        format="JPEG",
        options={"quality": 90},
    )
    # foodtag_id = models.ForeignKey(Foodtag, on_delete=models.CASCADE)
    # thematag_id = models.ForeignKey(Thematag, on_delete=models.CASCADE)
