from django.contrib import admin
from app.models import *
# Register your models here.


class vehicle_admin(admin.ModelAdmin):
    list_display = [field.name for field in vehicle._meta.get_fields()]
admin.site.register(vehicle, vehicle_admin)