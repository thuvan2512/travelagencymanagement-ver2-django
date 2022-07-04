# Generated by Django 4.0.3 on 2022-04-30 08:50

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_remove_user_role_user_is_customer_delete_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenews',
            options={'verbose_name': 'Image of new'},
        ),
        migrations.AlterModelOptions(
            name='imagetour',
            options={'verbose_name': 'Image of tour'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'New'},
        ),
        migrations.AlterModelOptions(
            name='tourinfo',
            options={'verbose_name': 'Tour information'},
        ),
        migrations.AlterField(
            model_name='imagenews',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='imagenews',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='travelapp.news'),
        ),
        migrations.AlterField(
            model_name='imagetour',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='imagetour',
            name='tour_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='travelapp.tourinfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Customer status'),
        ),
    ]