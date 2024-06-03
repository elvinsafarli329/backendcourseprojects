from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Movies(models.Model):
    year = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    recommender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    detail = RichTextField()
    image = models.ImageField(blank=True, null=True, verbose_name="add image")


    def __str__(self):
        return f"{self.name} | {self.year} | {self.category} | {self.detail}"
    

# class LikedMovie(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('user ', 'movie')

#     def __str__(self):
#         return f"{self.user.username} likes {self.movie.title}"