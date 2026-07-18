from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Memory(models.Model):
    memory_title = models.CharField(max_length=150)
    memory_text = models.TextField()
    register_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    user_registered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.memory_title
    
    class Meta:
        verbose_name_plural = "Memories"


def upload_gallery_image(instance, filename):
    return f"memory/{instance.memory.memory_title}/images/{filename}"

class MemoryGallery(models.Model):
    memory_image = models.ImageField(upload_to=upload_gallery_image)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name_plural = "Memory Galleries"

class MemoryLike(models.Model):
    user_liked = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True)
