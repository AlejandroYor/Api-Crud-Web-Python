
from django.urls import path 
from .views import MedicamentoView

urlpatterns = [
    path('medicamentos/', MedicamentoView.as_view(), name='medicamentos_list'),
    path('medicamentos/<int:id>', MedicamentoView.as_view(), name='medicamentos_process')
]
