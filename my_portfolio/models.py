from django.db import models
from taggit.managers import TaggableManager

class Pages(models.Model):
    name = models.CharField(max_length=64, blank=True, default="", unique=True)
    url = models.CharField(max_length=64, blank=True, unique=True)
    previous_url = models.CharField(max_length=64, blank=True)
    next_url = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.url

class Tecnology(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img_name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Tecnologies"

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img_name = models.CharField(max_length=32)
    description = models.TextField(max_length=512)
    url_github = models.CharField(max_length=512, null=True, blank=True)
    url_demo = models.CharField(max_length=512, null=True, blank=True)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Experience(models.Model):
    job = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    date_start = models.CharField(max_length=32)
    date_end = models.CharField(max_length=32)
    description = models.TextField(max_length=512)

    class Meta:
        verbose_name_plural = "Experiencies"

    def __str__(self):
        return self.job

class Education(models.Model):
    name = models.CharField(max_length=64)
    date_start = models.CharField(max_length=32)
    date_end = models.CharField(max_length=32)
    company = models.CharField(max_length=64)
    img_name = models.CharField(max_length=32)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.name
    
class Curriculum(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=512)

    class Meta:
        verbose_name_plural = "Curriculums"

    def __str__(self):
        return self.name