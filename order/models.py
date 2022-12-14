from django.db import models
from django.urls import reverse
from django.conf import settings

# to associate user to its "Contact Us" request
User = settings.AUTH_USER_MODEL

import users.models


# Create your models here.
class InternetPlans(models.Model):
    planName = models.CharField(max_length=50, verbose_name="Plan name")
    speed = models.CharField(max_length=20, verbose_name="Speed Mbps")
    price = models.FloatField(verbose_name="Monthly price in NIS")


    # def __str__(self):
    #     return self.planName

    # generate path to relevant plan
    # also this function create the button "view on site" on admin panel
    # if there is another name, no "get_absolute_url", so button will no exist
    def get_absolute_url(self):
        return reverse('plan', kwargs={'plan_id': self.pk})

    # rename the model in admin panel
    class Meta:
        verbose_name = 'Internet Package'
        verbose_name_plural = 'Internet Packages'

class ContactUsRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField(blank=True)
    subject = models.CharField(max_length=255)
    is_request_processed = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

