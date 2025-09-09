from rest_framework import viewsets
from .models import Kala
from .serializers import KalaSerializer

class KalaReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kala.objects.all()
    serializer_class = KalaSerializer
