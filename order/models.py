from django.db import models
from django.urls import reverse


# Create your models here.
class InternetPlans(models.Model):
    planName = models.CharField(max_length=50, verbose_name="Plan name")
    speed = models.CharField(max_length=20, verbose_name="Speed Mbps")
    price = models.FloatField(verbose_name="Monthly price in NIS")


    # def __str__(self):
    #     return self.planName

    # generate path to relevant plan
    # also this function create thw button "view on site" on admin panel
    # if there is another name, no "get_absolute_url", so button will no exist
    def get_absolute_url(self):
        return reverse('plan', kwargs={'plan_id': self.pk})

    # rename the model in admin panel
    class Meta:
        verbose_name = 'Internet Package'
        verbose_name_plural = 'Internet Packages'

class UserHelpRequest(models.Model):
    user_id = models.IntegerField(verbose_name= "User ID")
    message = models.TextField(blank=True)
    subject = models.CharField(max_length=255)
    is_request_open = models.BooleanField(default=False)

