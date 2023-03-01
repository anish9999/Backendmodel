# from django.shortcuts import render
# from rest_framework import viewsets
# from base.models import OccupancyCount
# from base.serializers import CountSerializer
# from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
# from django.shortcuts import get_object_or_404
# # Create your views here.
    
# class OCViewSet(viewsets.ModelViewSet):
#     queryset = OccupancyCount.objects.all().order_by("-id")
#     serializer_class = CountSerializer
#     lookup_field = 'Bus_id'

#     def retrieve(self, request, *args, **kwargs):
#         # bus_id = self.kwargs.get('Bus_id')
#         # instance = get_object_or_404(self.queryset, Bus_id=bus_id)
#         try:
#             pk_int = int('Bus_id')
#             instance = self.get_object()
#         except ValueError:
#             instance = get_object_or_404(self.queryset, Bus_id='Bus_id')
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from base.models import OccupancyCount
from base.serializers import CountSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import get_object_or_404


from rest_framework.decorators import action

class OCViewSet(viewsets.ModelViewSet):
    queryset = OccupancyCount.objects.all()
    serializer_class = CountSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    # ... other methods ...
    
    @action(detail=False, url_path='by-bus-id/(?P<bus_id>[^/.]+)', url_name='by_bus_id')
    def by_bus_id(self, request, bus_id=None):
        occupancy_counts = self.get_queryset().filter(Bus_id=bus_id)
        print(occupancy_counts)
        serializer = self.get_serializer(occupancy_counts, many=True)
        return Response(serializer.data)