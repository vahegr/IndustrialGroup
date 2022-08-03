from django.db import models
from django.utils import timezone


class HomeOption(models.Model):
    title = models.CharField(max_length=50)
    second_title = models.CharField(max_length=100, blank=True)
    icon = models.FileField(upload_to="images/home/icons", null=True, blank=True)
    image = models.ImageField(upload_to="images/home", null=True)
    created_time = models.DateTimeField(default=timezone.now)
    show_in_slider = models.BooleanField(default=False)
    show_in_page = models.BooleanField(default=False)
    url = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title


class TemporaryPost(models.Model):
    title = models.CharField(max_length=150)
    tips = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SideBar(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    services = models.BooleanField(default=False)
    common_questions = models.BooleanField(default=False)
    allowing = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Footer(models.Model):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    allowing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
