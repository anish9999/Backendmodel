from django.contrib import admin
from base.models import BusStopLoc,OccupancyCount


class UserAdmin(admin.ModelAdmin):
    list_display =('id','location','lat','lon')
    search_fields = ['location']
    
# Register your models here.
admin.site.register(BusStopLoc,UserAdmin)


class BaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Bus_id',
        'Total_count'# new field
    )
    search_fields = ['Bus_id']
    
    # def bus_id_count(self, obj):
    #     return f"{obj.Bus_id} - {obj.Total_count}"
    # bus_id_count.short_description = 'Bus ID - Total Count'  # custom column header

    
admin.site.register(OccupancyCount,BaseAdmin)