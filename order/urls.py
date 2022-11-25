from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('plan200/', plan200),
    path('plan600/', plan600),
    path('plan1000/', plan1000),
]