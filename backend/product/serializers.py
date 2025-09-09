from rest_framework import serializers
from .models import Kala

class KalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kala
        fields = '__all__'