from django import forms
from .models import Production, Machine
from users.models import User

class ProductionForm(forms.ModelForm):
    output_material = forms.ChoiceField(choices=[], required=True)
    material_color = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Production
        fields = ['production_date', 'machine', 'operator', 'output_material', 'material_color', 'quantity_kg', 'note']
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        machine = kwargs.pop('machine', None)  # Pass the selected machine dynamically
        super().__init__(*args, **kwargs)
        # Populate operator choices
        self.fields['operator'].queryset = User.objects.filter(role='employee')
        # Populate machine choices
        self.fields['machine'].queryset = Machine.objects.filter(is_active=True)
        # If a machine is provided, populate material and color choices
        if machine:
            self.populate_material_choices(machine)

    def populate_material_choices(self, machine):
        """Populate material and color choices based on the selected machine."""
        materials = machine.materials or {}
        self.fields['output_material'].choices = [(mat, mat) for mat in materials.keys()]
        self.fields['output_material'].widget.attrs.pop('disabled', None)

        # Prepopulate the color field based on the first material (if any)
        if materials:
            first_material = list(materials.keys())[0]
            colors = materials[first_material].get('color', [])
            self.fields['material_color'].choices = [(color, color) for color in colors]
        else:
            self.fields['material_color'].choices = []
        self.fields['material_color'].widget.attrs.pop('disabled', None)

    def clean(self):
        """Validate the selected material and color."""
        cleaned_data = super().clean()
        machine = cleaned_data.get('machine')
        output_material = cleaned_data.get('output_material')
        material_color = cleaned_data.get('material_color')

        if machine:
            # Validate the material
            materials = machine.materials or {}
            if output_material not in materials:
                raise forms.ValidationError(f"{output_material} is not valid for the selected machine.")
            # Validate the color
            valid_colors = materials[output_material].get('color', [])
            if material_color and material_color not in valid_colors:
                raise forms.ValidationError(f"{material_color} is not a valid color for {output_material}.")

        return cleaned_data

