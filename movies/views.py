from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import MoviesData

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyVeiwSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer

