from django.urls import path
from .views import MachineListView, MachineDetailView, MachineFormView, MachineDeleteView, ProductionCreateView, get_materials, get_materials_and_colors

urlpatterns = [
    path('', MachineListView.as_view(), name='machine_list'),               # hadi pour list all active machines
    path('<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),  
    path('create/', MachineFormView.as_view(), name='machine_create'),
    path('<int:pk>/update/', MachineFormView.as_view(), name='machine_update'), 
    path('<int:pk>/delete/', MachineDeleteView.as_view(), name='machine_delete'),


    path('production/', ProductionCreateView.as_view(), name='production_create'), 
    path('materials/<int:machine_id>/', get_materials_and_colors, name='get_materials_and_colors'),
]
