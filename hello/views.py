from django.shortcuts import render
from django.http import HttpResponse

from .models import WSNDetails, WSN, Sensor

import time
import json

# Create your views here.
def index(request):
    if request.method == "POST":
        dataJSON = request.body
        dataDict = json.loads(dataJSON)

        wsnDetails = {
            "wsn_id": dataDict.get("id"),
            "name": dataDict.get("name"),
            "location": dataDict.get("location")
        }

        newWSN = WSN.objects.create(**wsnDetails)

        sensors = dataDict.get("sensors")
        for sensor in sensors:
            sensorDetails = {
                "sensor_id": sensor.get("id"),
                "type": sensor.get("type"),
                "unit": sensor.get("unit"),
                "value": sensor.get("value"),
            }
            newSensor = Sensor.objects.create(**sensorDetails)
            w = WSNDetails(sensor=newSensor, wsn=newWSN)
            w.save()

        return HttpResponse('Hello {}'.format(w.when))
    else:
        return HttpResponse("")

def fetch(request, wsn_id):
    if request.method == "GET":
        wsnDetails = WSNDetails.objects.order_by("-when").filter(wsn__wsn_id=wsn_id)[0]
        sensors = []
        for sensor in wsnDetails.wsn.sensors.all():
            sensors.append({
                "id": sensor.sensor_id,
                "type": sensor.type,
                "unit": sensor.unit,
                "value": float(sensor.value)
            })
        dataDict = {
            "id": wsnDetails.wsn.wsn_id,
            "name": wsnDetails.wsn.name,
            "location": wsnDetails.wsn.location,
            "sensors": sensors
        }
        return HttpResponse(json.dumps(dataDict))
    else:
        return HttpResponse("")

