from rest_framework import serializers
from api.models import BusStopLoc

#create serializers here
class BSLSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BusStopLoc
        fields = "__all__"