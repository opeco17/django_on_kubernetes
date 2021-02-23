from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    writer = models.ForeignKey(get_user_model(), verbose_name='投稿者', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=200)
    text = models.TextField(verbose_name='本文')
    created_date = models.DateTimeField(verbose_name='投稿日', default=timezone.now)
    published_date = models.DateTimeField(verbose_name='公開日', blank=True, null=True)
    is_private = models.BooleanField(verbose_name='非公開', default=False, null=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return f'{self.title}'