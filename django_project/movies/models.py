from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class Movies(models.Model):
    year = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    recommender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    detail = RichTextField()
    image = models.FileField(blank=True, null=True, verbose_name="add image")


    def __str__(self):
        return f"{self.name} | {self.year} | {self.category} | {self.detail}"
    

class WriteComment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name="movie", related_name="comments")
    commenter = models.CharField(max_length=20, verbose_name="Name")
    comment_content = RichTextField(verbose_name="content")


    def __str__(self):
        return f"{self.commenter}"
    
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )


    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
