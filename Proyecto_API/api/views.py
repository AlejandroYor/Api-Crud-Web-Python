from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Medicamento
import json

# Create your views here.


class MedicamentoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
       
    def get(self, request, id=0):
        if (id > 0):
            medicamentos = list(Medicamento.objects.filter(id=id).values())
            if len(medicamentos) > 0:
                medicamento = medicamentos[0]
                datos = {'message': "Success", 'medicamento': medicamento}
            else:
                datos = {'message': "Medicamento not found..."}
            return JsonResponse(datos)
        else:
            medicamentos = list(Medicamento.objects.values())
            if len(medicamentos) > 0:
                datos = {'message': "Success", 'medicamentos': medicamentos}
            else:
                datos = {'message': "medicamentos not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Medicamento.objects.create(id=jd['id'], nombre=jd['nombre'], dosis=jd['dosis'], precio=jd['precio'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
        
    def put(self, request, id):
        jd = json.loads(request.body)
        medicamentos = list(Medicamento.objects.filter(id=id).values())
        if len(medicamentos) > 0:
            medicamento = Medicamento.objects.get(id=id)
            medicamento.id = jd['id']
            medicamento.nombre = jd['nombre']
            medicamento.dosis = jd['dosis']
            medicamento.precio = jd['precio']
            medicamento.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Medicamento not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        medicamentos = list(Medicamento.objects.filter(id=id).values())
        if len(medicamentos) > 0:
            Medicamento.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Medicamento not found..."}
        return JsonResponse(datos)



    
