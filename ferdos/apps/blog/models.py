from django.db import models
from apps.profiles.models import Visitor, Author, Staff, Administrator

# Create your models here.
class Memory(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    memory_title = models.CharField(max_length=50, blank=False, null=False)
    memory_text = models.TextField()
    memory_attachment = models.FileField(upload_to="attachments/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.memory_title


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=50, blank=False, null=False)
    article_text = models.TextField()
    article_attachment = models.FileField(upload_to="attachments/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.article_title


class Report(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    report_title = models.CharField(max_length=50, blank=False, null=False)
    report_text = models.TextField()
    report_attachment = models.FileField(upload_to="attachments/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.report_title


class Event(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=50, blank=False, null=False)
    event_text = models.TextField()
    event_attachment = models.FileField(upload_to="attachments/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.event_title