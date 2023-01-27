
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views.routeviews import BSLViewSet


router = routers.DefaultRouter()
router.register(r'busroutes', BSLViewSet)

urlpatterns = [
    path('',include(router.urls))
]