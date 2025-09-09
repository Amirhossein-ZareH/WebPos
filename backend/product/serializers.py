from rest_framework import serializers
from .models import Kala
from decimal import Decimal, InvalidOperation

class KalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kala
        fields = '__all__'