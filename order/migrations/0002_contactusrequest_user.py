# Generated by Django 4.1.3 on 2022-12-17 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_plan_id_profile_plan'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
