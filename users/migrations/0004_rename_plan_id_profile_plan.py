# Generated by Django 4.1.3 on 2022-12-16 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_plan_profile_plan_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='plan_id',
            new_name='plan',
        ),
    ]
