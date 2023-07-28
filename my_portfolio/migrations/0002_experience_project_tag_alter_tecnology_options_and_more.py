# Generated by Django 4.2.3 on 2023-07-28 19:39

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
                ('date_start', models.CharField(max_length=32)),
                ('date_end', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Experiencies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('img_name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=512)),
                ('url_github', models.CharField(max_length=32)),
                ('url_demo', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tecnology',
            options={'verbose_name_plural': 'Tecnologies'},
        ),
        migrations.AlterField(
            model_name='tecnology',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('date_start', models.CharField(max_length=32)),
                ('date_end', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
                ('img_name', models.CharField(max_length=32)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
    ]
