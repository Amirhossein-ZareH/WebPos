from rest_framework.routers import DefaultRouter
from .views import TafzilyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tafzily', TafzilyViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
