from rest_framework import viewsets
from .models import Tafzily
from .serializers import TafzilySerializer

class TafzilyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tafzily.objects.all()
    serializer_class = TafzilySerializer

