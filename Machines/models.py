from django.db import models
from users.models import User  

class Machine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    materials = models.JSONField(
        blank=True,
        null=True,
        help_text="Supported materials with attributes, e.g., {'Plastic A1': {'color': 'black'}, 'Plastic A2': {'color': 'white'}}"
    )

    metadata = models.JSONField(blank=True, null=True) 

    def __str__(self):
        return self.name

    def add_material(self, material_name, attributes):
        if not self.materials:
            self.materials = {}
        self.materials[material_name] = attributes
        self.save()

    def remove_material(self, material_name):
        if self.materials and material_name in self.materials:
            del self.materials[material_name]
            self.save()

    def list_materials(self):
        return self.materials or {}


class Production(models.Model):
    production_date = models.DateField()
    machine = models.ForeignKey(
        "Machine",
        on_delete=models.CASCADE,
        related_name="productions"
    ) 
    operator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'employee'},
        related_name="productions"
    ) 
    output_material = models.CharField(max_length=100)
    material_color = models.CharField(max_length=50,blank=True, null=True)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2) 
    note = models.TextField(blank=True, null=True)

    metadata = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.production_date} - {self.machine.name} - {self.output_material} ({self.material_color})"
