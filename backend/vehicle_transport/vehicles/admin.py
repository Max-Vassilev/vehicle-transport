from django.contrib import admin
from .models import VehicleTransportRequest

@admin.register(VehicleTransportRequest)
class VehicleTransportRequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'created_at', 'phone')
