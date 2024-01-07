# Generated by Django 4.2.3 on 2024-01-07 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0015_alter_pages_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date_end_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='education',
            name='date_end_year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='education',
            name='date_start_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='education',
            name='date_start_year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='experience',
            name='date_end_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='experience',
            name='date_end_year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='experience',
            name='date_start_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='experience',
            name='date_start_year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]