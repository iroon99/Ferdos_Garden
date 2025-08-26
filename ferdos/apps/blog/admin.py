from django.contrib import admin
from .models import Memory, Article, Report, Event

# Register your models here.
@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ['visitor', 'memory_title', 'modified_at', 'is_active']
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'article_title', 'modified_at', 'is_active']
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['staff', 'report_title', 'modified_at', 'is_active']
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['administrator', 'event_title', 'modified_at', 'is_active']