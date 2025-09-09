from rest_framework.routers import DefaultRouter
from .views import KalaReadOnlyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'kala', KalaReadOnlyViewSet, basename='kala')

urlpatterns = [
    path('', include(router.urls)),
]
