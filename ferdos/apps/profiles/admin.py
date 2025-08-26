from django.contrib import admin
from .models import Author, Visitor, Staff, Administrator

# Register your models here.
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'created_at', 'is_active']
    prepopulated_fields = {'slug':('name', 'family')}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'created_at', 'is_active']
    prepopulated_fields = {'slug':('name', 'family')}


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'employed_at', 'is_active']
    prepopulated_fields = {'slug':('name', 'family')}


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'employed_at', 'is_active']
    prepopulated_fields = {'slug':('name', 'family')}