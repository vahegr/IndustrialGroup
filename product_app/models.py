from django.db import models
from extensions.utils import jalali_converter
from django.urls import reverse
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


def my_slugify_function(content): return slugify(content, allow_unicode=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=100)
    coverImage = models.ImageField(upload_to='images/products', null=True)
    image = models.ImageField(upload_to='images/products')
    created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from=['title'], allow_unicode=True, slugify_function=my_slugify_function, blank=True)
    allowing = models.BooleanField(default=False)

    class Meta:                                                           # This method only shows the most recent posts
        ordering = ('-created',)                                          # other way in views ".order_by('-created')"

    def get_absolute_url(self):
        return reverse('product_app:product_detail', args=[self.id, self.slug])

    def jalali_price(self):
        return jalali_converter(str(self.price))

    def __str__(self):
        return self.title
