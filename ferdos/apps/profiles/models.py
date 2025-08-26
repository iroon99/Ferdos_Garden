from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=False, blank=False)
    family = models.CharField(max_length=25, null=False, blank=False)
    slug = models.SlugField(max_length=55, unique=True, default="")
    email = models.CharField(max_length=50, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.family


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    family = models.CharField(max_length=25, null=False, blank=False)
    slug = models.SlugField(max_length=55, unique=True, default="")
    email = models.CharField(max_length=50, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.family


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    family = models.CharField(max_length=25, null=False, blank=False)
    slug = models.SlugField(max_length=55, unique=True, default="")
    email = models.CharField(max_length=50, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    employed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.family


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    family = models.CharField(max_length=25, null=False, blank=False)
    slug = models.SlugField(max_length=55, unique=True, default="")
    email = models.CharField(max_length=50, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    employed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.family