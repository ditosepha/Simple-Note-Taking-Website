# Generated by Django 5.0.3 on 2024-04-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('data_created', models.DateField()),
            ],
            options={
                'db_table': 'NOTE DATA',
            },
        ),
    ]
