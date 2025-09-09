from django.contrib import admin
from .models import Kala

@admin.register(Kala)
class KalaAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'MoenCode', 'MoenName', 'Price', 'Mojode')
    search_fields = ('Code', 'Name', 'MoenCode', 'MoenName')
    list_filter = ('MoenCode', 'MoenName')
