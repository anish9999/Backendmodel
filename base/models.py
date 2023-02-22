from django.db import models

# Create your models here.

# Creating BusAddress Model
class BusStopLoc(models.Model): 
    lat = models.FloatField()
    lon = models.FloatField()
    location = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
# class BusOccupancyTracker(models.Model)
