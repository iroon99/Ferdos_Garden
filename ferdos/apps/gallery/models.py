from django.db import models
from apps.profiles.models import Visitor

# Create your models here.
class Photo(models.Model):
    registerer = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    photo_title = models.CharField(max_length=50)
    photo_attachment = models.FileField(upload_to="gallery/")
    photo_description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.photo_title


class Video(models.Model):
    registerer = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=50)
    video_attachment = models.FileField(upload_to="gallery/")
    video_description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.video_title