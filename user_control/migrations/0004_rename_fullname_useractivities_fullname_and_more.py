# Generated by Django 4.1.3 on 2023-02-20 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivities',
            old_name='fullName',
            new_name='fullname',
        ),
        migrations.AddField(
            model_name='useractivities',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_activities', to=settings.AUTH_USER_MODEL),
        ),
    ]
