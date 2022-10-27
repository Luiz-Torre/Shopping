# Generated by Django 4.1.2 on 2022-10-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teatro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('imagem', models.CharField(blank=True, max_length=50)),
                ('descricao', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'teatro',
            },
        ),
    ]