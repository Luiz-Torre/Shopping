# Generated by Django 4.1.2 on 2022-11-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_alter_loja_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='nome',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
