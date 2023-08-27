from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='post/%Y/%m/%d/')
    video = models.FileField(blank=True, null=True, upload_to='postvideos/%Y/%m/%d/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.image:
            max_size = 1 * 1024 * 1024 * 1024
            if self.image.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")
