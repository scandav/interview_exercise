from django.http import HttpResponse
from django.core import serializers
from .models import Measurement


def get_measurements(request):
    queryset = Measurement.objects

    patient = request.GET.get("patient")
    if patient is not None:
        queryset = queryset.filter(patient__name__icontains=patient)

    eye = request.GET.get("eye")
    if eye is not None:
        queryset = queryset.filter(eye=eye)

    data = serializers.serialize('json', queryset.all(), fields=('result', 'date', 'measurement_done'))

    return HttpResponse(data, content_type='application/json')