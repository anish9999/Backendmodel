from django.contrib import admin
from api.models import BusStopLoc


class UserAdmin(admin.ModelAdmin):
    list_display =('id','location','lat','lon')
    search_fields= ('location',)
    
    
# Register your models here.
admin.site.register(BusStopLoc,UserAdmin)