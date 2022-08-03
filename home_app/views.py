from django.shortcuts import render, redirect
from .models import TemporaryPost, HomeOption


def home(request):
    temporary_p = TemporaryPost.objects.filter(show=True)
    home_options = HomeOption.objects.filter(show_in_page=True)
    slider_options = HomeOption.objects.filter(show_in_slider=True)
    return render(request, 'home_app/index.html', context={"temp": temporary_p, "options": home_options, "slides": slider_options})
