# Generated by Django 3.2 on 2023-10-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_remove_userprofile_device_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
    ]
