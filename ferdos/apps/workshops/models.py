from django.db import models
from apps.profiles.models import Staff

# Create your models here.
class Workshop(models.Model):
    presenter = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=False, null=False)
    workshop_title = models.CharField(max_length=50, blank=False, null=False)
    workshop_place = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.workshop_title
    