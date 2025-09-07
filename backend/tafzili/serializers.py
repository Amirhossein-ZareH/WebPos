from rest_framework import serializers
from .models import Tafzily

class TafzilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tafzily
        fields = '__all__'
