# Generated by Django 4.2.3 on 2023-07-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0003_alter_project_url_demo_alter_project_url_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url_demo',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='url_github',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
