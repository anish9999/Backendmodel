from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import BSLViewSet


router = routers.DefaultRouter()
router.register(r'companies', BSLViewSet)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('',include(router.urls))
]
