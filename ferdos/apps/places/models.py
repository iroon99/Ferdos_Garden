from django.db import models
from apps.profiles.models import Staff

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=50, null=False, blank=False)
    presenter = models.ForeignKey(Staff, on_delete=models.CASCADE)
    ticket_price = models.IntegerField(null=False, blank=False)
    visit_day = models.CharField(max_length=15, null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.place_name

    