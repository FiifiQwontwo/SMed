from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
