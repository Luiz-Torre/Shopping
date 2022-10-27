# Generated by Django 4.1.2 on 2022-10-26 21:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='data_cadastro',
            field=models.DateField(default=datetime.date(2022, 10, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loja',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lojas', to='categoria.categoria'),
        ),
        migrations.AlterField(
            model_name='loja',
            name='descricao',
            field=models.CharField(max_length=150),
        ),
    ]
