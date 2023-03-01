from rest_framework import serializers
from base.models import BusStopLoc,OccupancyCount

 # create serializers here
class BSLSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BusStopLoc
        fields = "__all__"
        
class CountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OccupancyCount
        fields = "__all__"