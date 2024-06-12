from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class myBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    draft = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.color