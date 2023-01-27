from django.shortcuts import render
from rest_framework import viewsets
from api.models import BusStopLoc
from api.serializers import BSLSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
# Create your views here.


class BSLViewSet(viewsets.ModelViewSet):
    queryset = BusStopLoc.objects.all().order_by('-id')
    serializer_class = BSLSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]