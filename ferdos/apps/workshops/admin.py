from django.contrib import admin
from .models import Workshop

# Register your models here.
@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['presenter', 'workshop_title', 'workshop_place', 'capacity', 'start_date', 'end_date']