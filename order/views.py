from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

# Create your views here.
#menu = ["About us", "Contact us", "Log in | Register"]

menu = [
    {'title': "About us", 'url_name': 'about'},
    {'title': 'Contact us', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]


def index(request):
    # read plans info from DB
    plans = InternetPlans.objects.all()
    context = {
        'plans': plans,
        'menu': menu,
        'title': 'Choose Your plan',
    }
    return render(request, 'order/index.html', context = context)

def about(request):
    return render(request, 'order/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'order/contact.html', {'title': 'Contact Us'})

def login(request):
    return HttpResponse("Log in")

def support(request):
    return HttpResponse("Technical Support")

def upgrade_now(request, plan_id):
    return HttpResponse(f"Show info about plan with id = {plan_id}")

# def plan200(request):
#     return HttpResponse("plan 200mb")
#
# def plan600(request):
#     return HttpResponse("plan 600mb")
#
# def plan1000(request):
#     return HttpResponse("plan 1000mb")

#error 404 OUR custom message
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>error 404 custom message</h1>')