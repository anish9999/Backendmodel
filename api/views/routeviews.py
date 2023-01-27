from django.shortcuts import render
from rest_framework import viewsets
from api.models import BusStopLoc
from api.serializers import BSLSerializer
from rest_framework.permissions import IsAdminUser, BasePermission
# Create your views here.

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request , view):
        user = request.user
        if request.method == "GET":
            return True
        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False

class BSLViewSet(viewsets.ModelViewSet):
    queryset = BusStopLoc.objects.all().order_by('-id')
    serializer_class = BSLSerializer
    permission_classes = [WriteByAdminOnlyPermission]