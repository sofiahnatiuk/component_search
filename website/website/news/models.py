from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    thumbnail = models.TextField()
    cover_image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
