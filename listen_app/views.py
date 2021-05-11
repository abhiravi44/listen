from rest_framework import viewsets,generics
from listen_app.serializer import *
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render
from rest_framework import permissions


# Create your views here.
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PodcastList(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    # permission_classes = [permissions.IsAuthenticated]

class PodcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AudiobookList(generics.ListCreateAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    # permission_classes = [permissions.IsAuthenticated]

class AudiobookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    # permission_classes = [permissions.IsAuthenticated]
