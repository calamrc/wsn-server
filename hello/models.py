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
    battery = models.CharField(max_length=2)
    timestamp = models.CharField(max_length=30)
    active = models.CharField(max_length=10)
    rssi = models.CharField(max_length=10)
    sensors = models.ManyToManyField(Sensor, through="WSNDetails")

    def __str__(self):
        return self.name

class WSNDetails(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    wsn = models.ForeignKey(WSN, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now=True)

    # class Meta:
        # ordering = ("when",)

class Captcha(models.Model):
    state = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    image = models.ImageField(upload_to="captcha/")
