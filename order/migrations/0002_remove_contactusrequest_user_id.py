# Generated by Django 4.1.3 on 2022-12-04 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactusrequest',
            name='user_id',
        ),
    ]