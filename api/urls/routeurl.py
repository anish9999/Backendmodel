
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
<<<<<<<< HEAD:api/urls/routeurl.py
from api.views.routeviews import BSLViewSet
========
from base.views.routeviews import BSLViewSet
>>>>>>>> stages:base/urls/routeurl.py


router = routers.DefaultRouter()
router.register(r'busroutes', BSLViewSet)

urlpatterns = [
    path('',include(router.urls))
]