from django.db import models

# Create your models here.
class Message(models.Model):
    user_name = models.CharField(max_length=20, blank=False, verbose_name="نام کابر")
    user_family = models.CharField(max_length=20, blank=False, verbose_name="نام خانوادگی کابر")
    user_email = models.EmailField(max_length=40, blank=False, verbose_name="ایمیل")
    message_title = models.CharField(max_length=30, blank=False, verbose_name="عنوان پیام")
    message_text = models.TextField(blank=False, verbose_name="متن پیام")
    registered_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return self.message_title
