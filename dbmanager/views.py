import json
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from dbmanager.models import Prescription, Despensor


@csrf_exempt
def schedule(request):
    patient = Despensor.objects.filter(despensor_uid=request.POST.get("dispenser_uid")).first().patient
    sch = {
        'patient': str(patient),
        'schedule': []
    }
    for prescription in Prescription.objects.filter(user=patient):
        sch['schedule'].append(dict(drug=str(prescription.drug),
                                    schedule=[(p.medicine_count, p.timestamp, p.condition) for p in
                                              prescription.schedules.all()]))
    return JsonResponse(sch)


@csrf_exempt
def client_update(request):
    request.POST.get('')
    return JsonResponse({"error_code": 'success', 'message': 'updated count'})