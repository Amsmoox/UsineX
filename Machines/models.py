from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    metadata = models.JSONField(blank=True, null=True)  # JSON field for custom attributes (e.g., capacity, location)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True) 
    is_recyclable = models.BooleanField(default=True) 
    is_active = models.BooleanField(default=True) 

    metadata = models.JSONField(blank=True, null=True)  # JSON field for custom attributes (e.g., melting point, density)

    def __str__(self):
        return self.name
