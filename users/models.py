from django.db import models
from django.contrib.auth.models import User
from order.models import InternetPlans  # to-do
from PIL import Image


# Extending User Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField()

    # plan = models.ForeignKey(InternetPlans, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 128 or img.width > 128:
            new_img = (128, 128)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
