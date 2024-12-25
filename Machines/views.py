from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Machine, Material


# Flexible Model Form
class MachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'description', 'is_active', 'metadata']  # Common fields for create/update


@method_decorator(login_required, name='dispatch')
class MachineListView(View):
    def get(self, request):
        machines = Machine.objects.filter(is_active=True)  # Show active machines only
        return render(request, 'machines/machine_list.html', {'machines': machines})

@method_decorator(login_required, name='dispatch')
class MachineDetailView(View):
    def get(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        return render(request, 'machines/machine_list.html', {'machine': machine})


@method_decorator(login_required, name='dispatch')
class MachineFormView(FormView):
    template_name = 'machines/machine_form.html'
    form_class = MachineForm

    def get_initial(self):
        """Get initial data for the form (useful for updates)."""
        if 'pk' in self.kwargs:
            machine = get_object_or_404(Machine, pk=self.kwargs['pk'])
            return {
                'name': machine.name,
                'description': machine.description,
                'is_active': machine.is_active,
                'metadata': machine.metadata,
            }
        return super().get_initial()

    def form_valid(self, form):
        """Handle form submission for create or update."""
        if 'pk' in self.kwargs:
            machine = get_object_or_404(Machine, pk=self.kwargs['pk'])
            for field, value in form.cleaned_data.items():
                setattr(machine, field, value)
            machine.save()
        else:
            form.save()
        return redirect('machine_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

@method_decorator(login_required, name='dispatch')
class MachineDeleteView(View):
    def get(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        return render(request, 'machines/machine_form.html', {'machine': machine, 'delete': True})

    def post(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        machine.is_active = False  # Soft delete
        machine.save()
        return redirect('machine_list')
