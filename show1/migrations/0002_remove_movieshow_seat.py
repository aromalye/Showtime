# Generated by Django 4.1.4 on 2022-12-20 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieshow',
            name='seat',
        ),
    ]
