import datetime
import jdatetime
from django.db import models
from django_jalali.db import models as jmodels
from django.utils import timezone
from extensions.utils import jalali_converter
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify


def my_slugify_function(content): return slugify(content, allow_unicode=True)


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    created_time = models.DateTimeField(auto_now_add=True)
    created = jmodels.jDateField(auto_now_add=True)
    updated = jmodels.jDateField(auto_now=True)
    image = models.ImageField(upload_to='images/article', null=True)
    video = models.FileField(upload_to='videos/article', null=True)
    allowing = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=['title'], unique=True, allow_unicode=True, slugify_function=my_slugify_function, blank=True)
    hits = models.ManyToManyField(IpAddress, blank=True, related_name="hits")

    class Meta:
        ordering = ('-created_time',)

    def get_absolute_url(self):
        return reverse('article_app:article_detail', args=[self.id, self.slug])

    def jalali_number(self):
        return jalali_converter(str(self.created))

    def __str__(self):
        return self.title
