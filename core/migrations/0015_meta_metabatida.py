# Generated by Django 4.2.5 on 2023-11-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_atualizarmeta_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='metaBatida',
            field=models.BooleanField(default=False, verbose_name='Meta Batida'),
        ),
    ]
