from django.db import models

# Create your models here.
class Movies(models.Model):
    year = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    recommender = models.ForeignKey("auth.User", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} | {self.year}"