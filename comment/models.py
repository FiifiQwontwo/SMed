from django.conf import settings
from django.db import models
from post.models import Post


# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=200, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post} - {self.created_at}"

    @classmethod
    def get_comments_for_post(cls, post_id):
        return cls.objects.select_related('user').filter(post_id=post_id)

    @classmethod
    def get_comments_for_user(cls, user_id):
        return cls.objects.select_related('post').filter(user_id=user_id)
