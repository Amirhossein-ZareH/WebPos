from rest_framework import viewsets
from .models import Kala
from .serializers import KalaSerializer
from django.http import JsonResponse
from .models import Kala
class KalaReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kala.objects.all()
    serializer_class = KalaSerializer

def kala_list(request):
    # همه رکوردها یا 100 تا اول
    records = Kala.objects.all().values("Code", "Name")[:300]
    return JsonResponse(list(records), safe=False, json_dumps_params={'ensure_ascii': False})
