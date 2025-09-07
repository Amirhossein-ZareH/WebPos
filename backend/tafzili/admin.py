from django.contrib import admin
from .models import Tafzily

@admin.register(Tafzily)
class TafzilyAdmin(admin.ModelAdmin):
    list_display = ('tafzilycode', 'fname', 'lastname', 'city', 'tel', 'bad', 'change', 'mandeh', 'mandehtotal')
    search_fields = ('tafzilycode', 'fname', 'lastname', 'city', 'tel')
    list_filter = ('city', 'ozv')
    ordering = ('tafzilycode',)

    def mandehtotal(self, obj):
        bad = float(obj.bad) if obj.bad else 0
        atbar = float(obj.atbar) if obj.atbar else 0
        return bad - atbar
    mandehtotal.short_description = "مانده حساب"
