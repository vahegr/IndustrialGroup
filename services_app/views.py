from django.shortcuts import render
from services_app.models import Service


def services(request):
    service = Service.objects.filter(allowing=True)
    return render(request, 'services_app/services.html', context={'service': service})

