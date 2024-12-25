from django.urls import path
from .views import MachineListView, MachineDetailView, MachineFormView, MachineDeleteView

urlpatterns = [
    path('', MachineListView.as_view(), name='machine_list'),               # hadi pour list all active machines
    path('<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),  
    path('create/', MachineFormView.as_view(), name='machine_create'),
    path('<int:pk>/update/', MachineFormView.as_view(), name='machine_update'), 
    path('<int:pk>/delete/', MachineDeleteView.as_view(), name='machine_delete'),
]
