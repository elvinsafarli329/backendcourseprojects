from django.db import models


class portfolio(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    highest_education = models.CharField(max_length=70)
    school_name = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    work_experience = models.TextField()
    awards = models.TextField()
    skills = models.TextField()
    languages = models.TextField()
    hobbies = models.TextField()
    about = models.TextField()

    def __str__(self):
        return f"{self.name}'s resume"