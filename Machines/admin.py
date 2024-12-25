from django.contrib import admin
from .models import Machine, Material

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'metadata')
    search_fields = ('name', 'description', 'metadata')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'is_recyclable', 'is_active')
    list_filter = ('is_active', 'is_recyclable', 'category', 'metadata')
    search_fields = ('name', 'description', 'metadata')
