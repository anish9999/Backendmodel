from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('base.urls.routeurl')),
    path("bus_id/", include('base.urls.counturl')),
    path("", include('base.urls.urls'))
]