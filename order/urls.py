from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    #path('login/', login, name='login'),
    path('message_sent/', message_sent, name='message_sent'),
    path('plan_upgraded_message/', plan_upgraded_message, name='plan_upgraded_message'),

    # path('plan_upgraded_message/<int:plan_id>/', plan_upgraded_message, name='plan_upgraded_message'),

    path('plan/<int:plan_id>/', upgrade_now, name = 'plan')

    # path('about/', about),
    # path('plan200/', plan200),
    # path('plan600/', plan600),
    # path('plan1000/', plan1000),
]