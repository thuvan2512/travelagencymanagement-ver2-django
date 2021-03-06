# Generated by Django 4.0.3 on 2022-05-01 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0009_tag_tour_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('book_tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='travelapp.booktour')),
                ('payment_state', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0)),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bills', to='travelapp.typeofpayment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
