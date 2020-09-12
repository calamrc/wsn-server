from django.shortcuts import render
from django.http import HttpResponse

from .models import WSNDetails, WSN, Sensor, Captcha

import time
import json

# Create your views here.
def index(request):
    if request.method == "POST":
        try:
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

            return HttpResponse("Added")
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    else:
        return HttpResponse("Not Supported!")

def fetch(request, wsn_id):
    if request.method == "GET":
        try:
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
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    else:
        return HttpResponse("Not Supported!")


def captcha(request):
    if request.method == "POST":
        try:
            image = Captcha(isNew=True, image=request.FILES)
            image.save()

            return HttpResponse("Added")
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    elif request.method == "GET":
        try:
            catcha = Captcha.objects.get(pk=0)
            catcha.isNew = False
            catcha.save()
            return HttpResponse("Not Supported!")
        except Exception as e:
            return HttpResponse("Error: {}".format(e))

