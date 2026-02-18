from django.contrib import admin
from .models import Workshop, WorkshopGallery, WorkshopStatus

# Register your models here.
@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = [
        'workshop_title',
        'workshop_date_time',
        'place',
        'status',
        'is_active'
    ]
    
    
@admin.register(WorkshopStatus)
class WorshopStatusAdmin(admin.ModelAdmin):
    list_display = [
        'status_title'
    ]
    

@admin.register(WorkshopGallery)
class WorkshopGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'workshop',
        'picture'
    ]