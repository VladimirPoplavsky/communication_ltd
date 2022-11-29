from django.db import models
from django.urls import reverse


# Create your models here.
class InternetPlans(models.Model):
    planName = models.CharField(max_length=50)
    speed = models.CharField(max_length=20)
    price = models.FloatField()

    # def __str__(self):
    #     return self.planName

    # generate path to relevant plan
    def get_absolute_url(self):
        return reverse('plan', kwargs={'plan_id': self.pk})