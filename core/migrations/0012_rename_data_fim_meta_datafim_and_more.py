# Generated by Django 4.2.5 on 2023-11-12 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_meta_progresso_atual_alter_meta_valor_alvo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meta',
            old_name='data_fim',
            new_name='dataFim',
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='data_inicio',
            new_name='dataInicio',
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='progresso_atual',
            new_name='progressoAtual',
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='tipo_meta',
            new_name='tipoMeta',
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='unidade_medida',
            new_name='unidadeMedida',
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='valor_alvo',
            new_name='valorAlvo',
        ),
    ]
