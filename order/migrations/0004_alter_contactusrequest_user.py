# Generated by Django 4.1.3 on 2022-12-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_plan_id_profile_plan'),
        ('order', '0003_alter_contactusrequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusrequest',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
