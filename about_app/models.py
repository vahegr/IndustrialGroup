from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    first_division = models.BooleanField(default=False)
    second_division = models.BooleanField(default=False)
    third_division = models.BooleanField(default=False)
    allowing = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AboutPageImage(models.Model):
    image = models.ImageField(upload_to="images/about")
    allowing = models.BooleanField(default=False)
