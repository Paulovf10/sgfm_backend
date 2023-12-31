# Generated by Django 4.2.5 on 2023-09-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gestor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=50, null=True, verbose_name="Nome"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("senha", models.CharField(max_length=18, verbose_name="Senha")),
                (
                    "dtNascimento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Nascimento"
                    ),
                ),
                (
                    "endereco",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Endereço"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "empresa",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Empresa"
                    ),
                ),
                (
                    "cargo",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Cargo"
                    ),
                ),
                (
                    "equipe",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Equipe"
                    ),
                ),
                (
                    "foto",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="perfil",
                        verbose_name="Foto de perfil",
                    ),
                ),
            ],
            options={"verbose_name": "Gestor", "verbose_name_plural": "1. Gestores",},
        ),
    ]
