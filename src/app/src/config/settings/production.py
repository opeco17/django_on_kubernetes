from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'maindb',
        'USER': 'root',
        'PASSWORD': 'root',
        "HOST": 'database',
        "PORT": '3306',
        'ATOMIC_REQUESTS': True,
    }
}