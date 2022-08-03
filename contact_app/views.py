from django.shortcuts import render
from .models import ContactInfo, Opinion


def contact_us(request):
    messages = {"message": []}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        message = request.POST.get('message')
        Opinion.objects.create(name=name, email=email, sub=sub, message=message)

    c_info = ContactInfo.objects.get(allowing=True)
    return render(request, 'contact_app/contact.html', context={'info': c_info})
