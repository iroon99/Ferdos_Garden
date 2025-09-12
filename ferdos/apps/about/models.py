from django.db import models

class VisitDay(models.Model):
    day_name = models.CharField(max_length=12, blank=False)
    
    def __str__(self):
        return self.day_name

class VisitRule(models.Model):
    rule_title = models.CharField(max_length=20, blank=False)
    rule_description = models.TextField(blank=False)
    
    def __str__(self):
        return self.rule_title
    
class Part(models.Model):
    part_name = models.CharField(max_length=15, blank=False)
    
    def __str__(self):
        return self.part_name

class Place(models.Model):
    place_title = models.CharField(max_length=30, blank=False)
    place_picture = models.FileField(upload_to='attachments/articles')
    visit_day = models.ManyToManyField(VisitDay, blank=False)
    visit_time = models.TimeField(null=False)
    visit_rules = models.ManyToManyField(VisitRule, blank=False)
    place_part = models.ForeignKey(Part, null=False, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    ticket_required = models.BooleanField(null=False, blank=False, default=False)
    
    def __str__(self):
        return self.place_title
    
class VisitorGroup(models.Model):
    group_title = models.CharField(max_length=15, blank=False)
    
    def __str__(self):
        return self.group_title
    
class Ticket(models.Model):
    ticket_title = models.CharField(max_length=20, blank=False)
    group = models.ForeignKey(VisitorGroup, null=False, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=False, on_delete=models.CASCADE)
    price = models.IntegerField() # Needs validator
    
    def __str__(self):
        return self.ticket_title
