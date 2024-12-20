# Generated by Django 5.1.3 on 2024-11-09 10:42

import django.db.models.deletion
import hotel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('map_link', models.URLField(verbose_name='Map Link')),
                ('description', models.TextField()),
                ('included', models.TextField(help_text='Services included in the package')),
                ('excluded', models.TextField(help_text='Services not included in the package')),
                ('program', models.TextField(help_text='Hotel program or itinerary')),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('duo', 'Duo'), ('family', 'Family'), ('luxury', 'Luxury'), ('deluxe', 'Deluxe')], max_length=10)),
                ('airport_transfer', models.BooleanField(default=False)),
                ('safety_box', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('spa_sauna', models.BooleanField(default=False)),
                ('pet_allowed', models.BooleanField(default=False)),
                ('free_wifi', models.BooleanField(default=False)),
                ('air_dryer', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('laundry_service', models.BooleanField(default=False)),
                ('king_size_bed', models.BooleanField(default=False)),
                ('front_desk', models.BooleanField(default=False)),
                ('living_area', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=1, help_text='Rating out of 10', max_digits=3)),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, '1 Stars'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars'), (6, '6 Stars')], default=1)),
                ('image1', models.ImageField(upload_to=hotel.models.image_upload)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=hotel.models.image_upload)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=hotel.models.image_upload)),
                ('category', models.CharField(blank=True, choices=[('best_sale', 'Best Sale'), ('promotion', 'Promotion'), ('top', 'Top')], max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('number_of_adults', models.PositiveSmallIntegerField(default=1, verbose_name='Number of Adults (18+)')),
                ('amount_per_adult', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount_adult', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('number_of_children', models.PositiveSmallIntegerField(default=0, verbose_name='Number of Children (Under 18)')),
                ('amount_per_child', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_amount_children', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.hotel')),
            ],
        ),
    ]
