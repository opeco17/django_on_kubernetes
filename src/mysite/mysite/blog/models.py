from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    writer = models.CharField(verbose_name="投稿者", max_length=100)
    title = models.CharField(verbose_name="タイトル", max_length=200)
    text = models.TextField(verbose_name="本文")
    created_date = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="公開日", blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return f'id:{self.id}\nwriter:{self.writer}\ntitle:{self.title}\ntext:{self.text}'