from rest_framework import serializers
from .models import MoviesData

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        field = ['id','name','duration','rating']

        