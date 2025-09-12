from django.contrib import admin
from .models import VisitDay, VisitRule, Place, VisitorGroup, Ticket, Part
    
@admin.register(VisitDay)
class VisitDayAdmin(admin.ModelAdmin):
    list_display = [
        'day_name'
    ]

@admin.register(VisitRule)
class VisitRuleAdmin(admin.ModelAdmin):
    list_display = [
        'rule_title'
    ]

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = [
        'part_name'
    ]

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'place_title',
        'registered_at'
    ]
    
@admin.register(VisitorGroup)
class VisitorGroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_title'
    ]

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'ticket_title',
        'place',
        'price'
    ]