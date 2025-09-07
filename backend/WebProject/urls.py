from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tafzili.urls')),  # ← توجه به اسم اپ
    path('', TemplateView.as_view(template_name='Home.html')),
]
