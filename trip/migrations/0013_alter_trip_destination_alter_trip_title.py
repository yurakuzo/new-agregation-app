# Generated by Django 4.2.5 on 2023-12-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0012_alter_trip_max_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='trip',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]
