from django.db import models

# Create your models here.
class Sensor(models.Model):
    sensor_id = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2)

class WSN(models.Model):
    wsn_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    sensors = models.ManyToManyField(Sensor, through="WSNDetails")

    def __str__(self):
        return self.name

class WSNDetails(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    wsn = models.ForeignKey(WSN, on_delete=models.CASCADE)

