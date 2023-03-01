from django.db import models

# Create your models here.

# Creating BusAddress Model
class BusStopLoc(models.Model): 
    lat = models.FloatField()
    lon = models.FloatField()
    location = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location
   
    
# class BusOccupancyTracker(models.Model)
class OccupancyCount(models.Model):
    Bus_id  = models.CharField(max_length = 100)
    Total_count = models.IntegerField()
    
    def __str__(self):
        return f"{self.Bus_id} - {self.Total_count}"