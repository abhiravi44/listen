from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Podcast(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    host=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Audiobook(models.Model):
    duration=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    narrator=models.CharField(max_length=100)

    def __str__(self):
        return self.title
