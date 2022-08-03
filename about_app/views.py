from django.shortcuts import render
from .models import AboutUs, AboutPageImage


def about_us(request):
    first_d = AboutUs.objects.filter(first_division=True, allowing=True)[:2]
    second_d = AboutUs.objects.filter(second_division=True, allowing=True)[:3]
    third_d = AboutUs.objects.filter(third_division=True, allowing=True)[:4]
    page_image = AboutPageImage.objects.get(allowing=True)
    return render(request, 'about_app/about.html', context={'fd': first_d, 'sd': second_d, 'td': third_d, 'image': page_image})
