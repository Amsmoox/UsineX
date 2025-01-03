from django.contrib import admin
from .models import Machine, Production

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'materials', 'metadata')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('production_date', 'machine', 'operator', 'output_material', 'quantity_kg', 'created_at')
    list_filter = ('production_date', 'machine', 'operator')
    search_fields = ('output_material', 'note', 'metadata')
    ordering = ('-production_date',)