# Generated by Django 3.2.13 on 2023-10-19 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20231005_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meta',
            old_name='descircao',
            new_name='descricao',
        ),
    ]
