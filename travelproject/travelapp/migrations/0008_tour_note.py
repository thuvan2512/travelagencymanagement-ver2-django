# Generated by Django 4.0.3 on 2022-05-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0007_alter_news_content_alter_tourinfo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
