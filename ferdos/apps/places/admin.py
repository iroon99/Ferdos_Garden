from django.contrib import admin
from .models import Place

# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'presenter', 'ticket_price', 'visit_day', 'is_active']