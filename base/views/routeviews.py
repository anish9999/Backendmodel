from django.shortcuts import render
from rest_framework import viewsets
from base.models import BusStopLoc
from base.serializers import BSLSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class BSLViewSet(viewsets.ModelViewSet):
    queryset = BusStopLoc.objects.all().order_by('-id')
    serializer_class = BSLSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]
    