from rest_framework import serializers
from .models import juego,consola,figura


class juegoSerializer(serializers.ModelSerializer):
    class Meta:
        model=juego
        fields='__all__'

class consolaSerializer(serializers.ModelSerializer):
    class Meta:
        model=consola
        fields='__all__'

class figuraSerializer(serializers.ModelSerializer):
    class Meta:
        model=figura
        fields='__all__'