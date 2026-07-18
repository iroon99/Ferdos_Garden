from django.contrib import admin
from .models import Memory, MemoryGallery

# Register your models here.
@admin.register(Memory)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'memory_title',
        'register_date',
        'is_active',
        'user_registered'
    ]

@admin.register(MemoryGallery)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'memory',
        'memory_image' 
    ]
