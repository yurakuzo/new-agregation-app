# Generated by Django 4.2.5 on 2023-09-15 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='traveller',
            name='first_name',
            field=models.CharField(max_length=35, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='traveller',
            name='last_name',
            field=models.CharField(max_length=35, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='traveller',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(12)]),
        ),
    ]