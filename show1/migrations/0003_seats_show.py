# Generated by Django 4.1.4 on 2022-12-20 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show1', '0002_remove_movieshow_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='show1.movieshow'),
        ),
    ]
