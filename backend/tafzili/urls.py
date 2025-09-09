from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TafzilyReadOnlyViewSet

router = DefaultRouter()
router.register(r'tafzili', TafzilyReadOnlyViewSet, basename='tafzili')

urlpatterns = [
    path('', include(router.urls)),
]
