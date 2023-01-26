from rest_framework import serializers
from api.models import BusStopLoc

#create serializers here
class BSLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusStopLoc
        fields = "__all__"