from api.views import view
from django.urls import path

urlpatterns = [
    path('', view.getRoutes)
]
