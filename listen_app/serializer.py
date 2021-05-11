from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','name','duration','created_at']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model=Podcast
        fields=['id','name','duration','created_at','host']


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Audiobook
        fields=['id','author','title','narrator','duration','created_at',]
