# Generated by Django 4.1.2 on 2022-10-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroFilme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'db_table': 'GeneroFilme',
            },
        ),
    ]