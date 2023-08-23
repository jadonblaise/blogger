from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=225)
    tagline = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Entry(models.Model):
    body_text = models.TextField()
