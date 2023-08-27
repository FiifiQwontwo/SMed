from django.conf import settings
from django.db import models
from post.models import Post


# Create your models here.

class Repost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reposted by {self.user} on {self.post} at {self.created_at}"
