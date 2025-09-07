from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Tafzily
from .serializers import TafzilySerializer

class TafzilyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    فقط نمایش داده‌ها بدون امکان ایجاد یا ویرایش.
    GET /api/tafzily/ : لیست همه رکوردها
    GET /api/tafzily/<id>/ : جزئیات رکورد
    """
    queryset = Tafzily.objects.all()
    serializer_class = TafzilySerializer
    permission_classes = [AllowAny]  # فقط برای تست، بعداً تغییر بده
