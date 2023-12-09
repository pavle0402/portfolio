from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import DetailView
from .models import Project
import requests
from decouple import config


def HomeView(request):
    return render(request, "pages/home.html", {})

def AboutMeView(request):
    return render(request, "pages/about.html", {})

def PortfolioView(request):
    return render(request, "pages/portfolio.html", {})

def ServicesView(request):
    return render(request, "pages/services.html", {})

def validate_recaptcha(secret_key, response):
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': secret_key,
        'response': response
    }
    result = requests.post(url, data=data)
    return result.json().get("success", False)


def ContactView(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST["email"]
        message = request.POST["message"]

        recaptcha_response = request.POST.get("g-recaptcha-response")
        secret_key = config("SECRET_KEY")
        is_valid_captcha = validate_recaptcha(secret_key, recaptcha_response)

        if is_valid_captcha: 
            send_mail(
                f'Message from {name}. - {email}',
                message,
                email,
                ['pavles2002@gmail.com', 'jopasto02@gmail.com']
            )

            return render(request, 'pages/contact.html', {'name': name, 'message':message})
        else:
            return render(request, 'pages/contact.html', {'captcha_error': True})
    return render(request, 'pages/contact.html', {})



class ProjectDetailView(DetailView):
    model = Project 
    template_name = "pages/project_preview.html"
    context_object_name = "project"