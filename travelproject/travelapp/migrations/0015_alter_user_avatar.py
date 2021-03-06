# Generated by Django 4.0.3 on 2022-05-02 12:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0014_alter_booktour_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
