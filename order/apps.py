from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    # rename column in the admin panel
    verbose_name = "Available Internet Plans"