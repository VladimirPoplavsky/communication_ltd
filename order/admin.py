from django.contrib import admin

# Register your models here.
from .models import *

class InternetPlansAdmin(admin.ModelAdmin):
    list_display = ('id', 'planName', 'speed', 'price')
    list_display_links = ('id', 'planName')
    search_fields = ('id', 'planName', 'speed', 'price')

admin.site.register(InternetPlans, InternetPlansAdmin)
