from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'maindb',
        'USER': 'root',
        'PASSWORD': 'root',
        "HOST": '127.0.0.1',
        "PORT": '30100',
        'ATOMIC_REQUESTS': True,
    }
}