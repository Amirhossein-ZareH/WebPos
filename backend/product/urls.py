from rest_framework.routers import DefaultRouter
from .views import KalaReadOnlyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'kala', KalaReadOnlyViewSet, basename='kala')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import kala_list

urlpatterns = [
    path("kala/", kala_list, name="kala-list"),
]
