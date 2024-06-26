# Generated by Django 5.0.4 on 2024-04-20 05:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996-XXX-XXXXXX'.", regex='^\\+996-\\d{3}-\\d{6}$')])),
                ('number_of_people', models.PositiveIntegerField()),
                ('additional_comments', models.TextField(blank=True, null=True)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], default='pending', max_length=10)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='tours.tour')),
            ],
        ),
    ]
