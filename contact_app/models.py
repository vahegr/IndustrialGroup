from django.db import models


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20)
    second_phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.CharField(max_length=50)
    street_address = models.TextField(max_length=1500)
    google_map_url = models.CharField(max_length=2000, null=True)
    allowing = models.BooleanField(default=False)


class Opinion(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    sub = models.CharField(max_length=70)
    message = models.TextField(max_length=150)
    allowing = models.BooleanField(default=False)

    def __str__(self):
        return self.sub

