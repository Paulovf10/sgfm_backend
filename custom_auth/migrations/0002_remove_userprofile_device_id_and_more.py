# Generated by Django 4.2.5 on 2023-10-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_auth", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="device_id",),
        migrations.RemoveField(model_name="userprofile", name="is_active",),
        migrations.RemoveField(model_name="userprofile", name="is_premium",),
        migrations.RemoveField(model_name="userprofile", name="is_staff",),
        migrations.AddField(
            model_name="userprofile",
            name="addres",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="CPF"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="profile_picture",
            field=models.FileField(
                blank=True, null=True, upload_to="perfil", verbose_name="Foto de perfil"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="type_user",
            field=models.SmallIntegerField(
                blank=True,
                choices=[(1, "Administrador"), (2, "Gerente"), (3, "Colaborador")],
                null=True,
                verbose_name="Tipo de usuário",
            ),
        ),
        migrations.DeleteModel(name="UserAddress",),
    ]
