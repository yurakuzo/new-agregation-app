# Generated by Django 4.2.5 on 2023-12-10 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0010_trip_difficulty'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='trip_images/')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trip.trip')),
            ],
        ),
    ]