from django.shortcuts import render, redirect
from .models import dht,sensor_data
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.conf import settings
from django.http import HttpResponse,Http404
import os
from datetime import datetime
# Create your views here.
# def sensor_upload(request):
#     if request.method == 'POST':
#         temp = request.POST.get('temperature')
#         hum = request.POST.get('humidity')
#         dht.objects.create(temperature=temp, humidity=hum)
#         return redirect('sensor_data')
#     return render(request, 'sensor_upload.html')
# def sensor_data(request):
#     data = dht.objects.all().order_by('-recorded_at')
#     return render(request, 'sensor_data.html',{'data':data})
@csrf_exempt
def upload_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            
            if temperature is not None and humidity is not None:
                sensor_data.objects.create(temperature=temperature, humidity=humidity,timestamp=datetime.now())
                return JsonResponse({'message': 'success'}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'message': 'notComplit'},status = 400 ,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'error': 'jsonanalfail', 'detail': str(e)}, status=400, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'notpost'}, status=405, json_dumps_params={'ensure_ascii': False})
def show_data(request):
    records = sensor_data.objects.order_by('-timestamp')[:10]
    return render(request, 'ESP32_sensor_data.html', {'records': records})