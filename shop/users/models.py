from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='urls_images', blank=True, null=True)

    def __str__(self):
        return self.username
