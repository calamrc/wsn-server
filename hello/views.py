from django.shortcuts import render
from django.http import HttpResponse

# from .models import WSNDetails

import time
import json


# Create your views here.
def index(request):
    if request.method == "POST":
        # dataJSON = request.body
        # dataDict = json.loads(dataJSON)
        # data = WSNDetails.objects.create(**dataDict)
        return HttpResponse('Hello {}'.format(request.body))

    return render(request, "index.html")

