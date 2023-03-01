from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from base.views.countviews import OCViewSet


router = routers.DefaultRouter()
router.register(r'people_count', OCViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('<str:Bus_id>/', OCViewSet.as_view({'get': 'retrieve'})),
]