from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
        
    self_introduction = models.TextField(verbose_name='自己紹介', blank=True, null=True)