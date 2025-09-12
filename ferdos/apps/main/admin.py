from django.contrib import admin
from .models import Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'message_title',
        'user_name',
        'user_family',
        'user_email',
        'registered_at'
    ]