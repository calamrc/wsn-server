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
    elif request.method  == "GET":
        try:
            wsnDetails = WSNDetails.objects.all()
            nodes = {
                "nodes": [],
            }
            for wsn in wsnDetails.wsn.all():
                wsn_id = wsn.wsn_id
                if not(wsn_id in nodes["nodes"]):
                    nodes["nodes"].append(wsn_id)

            return HttpResponse(json.dumps(nodes))
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    else:
        return HttpResponse("index {}".format(request.method))

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
        return HttpResponse("fetch {}".format(request.method))


def captcha_text(request):
    if request.method == "POST":
        try:
            captcha = Captcha.objects.all().order_by("-id")[0]
            captcha.text = request.body
            captcha.state = "new_text"
            captcha.save()
            return HttpResponse(captcha.text)
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    elif request.method == "GET":
        try:
            captcha = Captcha.objects.all().order_by("-id")[0]
            if captcha.state == "new_text":
                captcha.state = "old_text"
                captcha.save()
                return HttpResponse("captcha_text: {}".format(captcha.text))
            else:
                return HttpResponse(captcha.state)
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    else:
        return HttpResponse("captcha {}".format(request.method))


def captcha(request):
    if request.method == "POST":
        try:
            image = Captcha(state="new_image", image=request.FILES["media"])
            image.save()

            return HttpResponse(image.state)
        except Exception as e:
            return HttpResponse("Error: {}".format(e), status=204)
    elif request.method == "GET":
        try:
            captcha = Captcha.objects.all().order_by("-id")[0]
            if captcha.state == "new_image":
                captcha.state = "old_image"
                captcha.save()
                return HttpResponse(captcha.image, status=200, content_type="image/png")
            else:
                return HttpResponse(status=204)
        except Exception as e:
            return HttpResponse("Error: {}".format(e))
    else:
        return HttpResponse("captcha {}".format(request.method))

