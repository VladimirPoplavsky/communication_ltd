from django.db import models

# Create your models here.
class InternetPlans(models.Model):
    planName = models.CharField(max_length=50)
    speed = models.CharField(max_length=20)
    price = models.FloatField()


