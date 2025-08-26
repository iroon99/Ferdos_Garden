from django.contrib import admin
from .models import Video, Photo

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['registerer', 'photo_title', 'photo_attachment', 'uploaded_at', 'is_active']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['registerer', 'video_title', 'video_attachment', 'uploaded_at', 'is_active']