from django.contrib import admin

from .models import WSNDetails, WSN, Sensor

# Register your models here.
admin.site.register(WSNDetails)
admin.site.register(WSN)
admin.site.register(Sensor)
