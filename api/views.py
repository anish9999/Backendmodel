from django.shortcuts import render
from rest_framework import viewsets
from api.models import BusStopLoc
from api.serializers import BSLSerializer
# Create your views here.


class BSLViewSet(viewsets.ModelViewSet):
    queryset = BusStopLoc.objects.all()
    serializer_class = BSLSerializer
