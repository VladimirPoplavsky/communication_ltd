import profile

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

import users.models
from .forms import *
from order.models import *
from users.models import *


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

    if request.user.is_authenticated:
        userPlan = request.user.profile.plan.id
        context = {
            'plans': plans,
            'menu': menu,
            'title': 'Choose Your plan',
            'userPlan': userPlan
        }
    else:
        context = {
            'plans': plans,
            'menu': menu,
            'title': 'Choose Your plan',
        }
    return render(request, 'order/index.html', context = context)

def about(request):
    return render(request, 'order/about.html', {'menu': menu, 'title': 'About Us'})

def message_sent(request):
    return render(request, 'order/message_sent.html', {'menu': menu, 'title': 'Thank You'})


def contact(request):
    # if user input is incorrect - he will get back to "Contact Us" form
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                form.save()
                return redirect('message_sent')
            except:
                form.add_error(None, 'There is occurring some error, when creating request, please try later')
    else:
        form = ContactUsForm()
    return render(request, 'order/contact.html', {'form': form, 'menu': menu, 'title': 'Contact Us'})


def login(request):
    return HttpResponse("Log in")

def support(request):
    return HttpResponse("Technical Support")

def upgrade_now(request, plan_id):
    plan = get_object_or_404(InternetPlans, pk = plan_id)

    # global variable "selectedPlan" belongs to global scope for making update  plan_id
    # in Profile model when user buy new internet plan
    global selectedPlan
    selectedPlan = plan_id

    context = {
        'plan': plan,
        'menu': menu,
        'title': plan.speed,
        'plan_selected': plan_id
    }

    return render(request, 'order/plan.html', context = context)


def plan_upgraded_message(request):
    # update current internet plan after the user press "Buy now"

    record = Profile.objects.get(id = request.user.profile.id)
    record.plan_id = selectedPlan # selectedPlan is defined in function upgrade_now(request, plan_id)
    record.save()
    return render(request, 'order/plan_successfully_upgraded.html', {'menu': menu, 'title': 'Congratulations'})


#error 404 OUR custom message
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>error 404 custom message </h1>')