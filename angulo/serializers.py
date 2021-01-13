from .models import Angulo
from rest_framework import serializers

class AnguloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angulo
        fields = ['angle']

class AllAnguloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angulo
        fields = ['id', 'hour', 'minute', 'angle', 'date']