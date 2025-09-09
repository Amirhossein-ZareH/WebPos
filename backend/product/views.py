# tafzili/views.py
from rest_framework import viewsets
from .models import Kala
from .serializers import KalaSerializer
from rest_framework.permissions import AllowAny

class KalaReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kala.objects.all()
    serializer_class = KalaSerializer
    permission_classes = [AllowAny]
# tafzili/views.py
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Kala
from .serializers import KalaSerializer

class KalaPagination(PageNumberPagination):
    page_size = 50  # هر صفحه 50 رکورد
    page_size_query_param = 'page_size'
    max_page_size = 100

class KalaReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kala.objects.all()
    serializer_class = KalaSerializer
    pagination_class = KalaPagination