# Generated by Django 4.2.3 on 2023-09-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0011_curriculum_alter_project_options_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
