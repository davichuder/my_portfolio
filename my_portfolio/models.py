from django.db import models
from taggit.managers import TaggableManager


class Tecnology(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img_name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Tecnologies"

class Experience(models.Model):
    job = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    date_start = models.CharField(max_length=32)
    date_end = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    class Meta:
        verbose_name_plural = "Experiencies"

class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img_name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    url_github = models.CharField(max_length=512, null=True, blank=True)
    url_demo = models.CharField(max_length=512, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

class Education(models.Model):
    name = models.CharField(max_length=32)
    date_start = models.CharField(max_length=32)
    date_end = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    img_name = models.CharField(max_length=32)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "Education"