from django.db import models

# Create your models here.
class dht(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recorded_at} | 溫度: {self.temperature} | 濕度: {self.humidity})"
# class SensorData(models.Model):
#     temperature = models.FloatField()
#     humidity = models.FloatField()
#     recorded_at = models.DateTimeField(auto_now_add=True)
class sensor_data(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'sensor_data'
        managed = False
    def __str__(self):
        return f"{self.timestamp}: {self.temperature}/{self.humidity}"