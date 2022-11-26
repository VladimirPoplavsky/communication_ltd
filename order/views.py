from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

# Create your views here.
menu = ["About us", "Contact us", "Log in | Register"]

def index(request):
    plans = InternetPlans.objects.all()
    return render(request, 'order/index.html', {'plans': plans, 'menu': menu, 'title': 'Choose Your plan:'})

def about(request):
    return render(request, 'order/about.html', {'title': 'About'})

def plan200(request):
    return HttpResponse("plan 200mb")

def plan600(request):
    return HttpResponse("plan 600mb")

def plan1000(request):
    return HttpResponse("plan 1000mb")

#error 404 OUR custom message
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>error 404 custom message</h1>')