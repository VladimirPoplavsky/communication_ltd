from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("login/register | packages info")

def about(request):
    return HttpResponse("About the company")

def plan200(request):
    return HttpResponse("plan 200mb")

def plan600(request):
    return HttpResponse("plan 600mb")

def plan1000(request):
    return HttpResponse("plan 1000mb")

#error 404 OUR custom message
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>error 404 custom message</h1>')