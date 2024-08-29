from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from django.shortcuts import render
from .models import Contact, Project

def contact(request):
    projects = Project.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        if len(name) > 1 and len(name) < 30 and len(email) > 1 and len(email) < 30 and len(number) > 9 and len(number) < 13:
            Contact.objects.create(name=name, email=email, content=content, number=number)
            messages.success(request, 'Thank You for contacting me!! Your message has been saved')
        else:
            messages.error(request, 'Please check your input fields and try again.')

    return render(request, 'home.html', {'projects': projects})

