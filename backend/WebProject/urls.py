from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, "Home.html")

def tafzili_page(request):
    return render(request, "Tafzily.html")

def kala_page(request):
    return render(request, "product.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tafzili.urls')),
    path('api/', include('product.urls')),
    path('', index, name="home"),
    path('Tafzily/', tafzili_page, name="Tafzily-page"),
    path('product/', kala_page, name="product-page"),
]
