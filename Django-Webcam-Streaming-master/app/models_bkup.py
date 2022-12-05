from django.db import models

# Create your models here.
class vehicle(models.Model):
    vehicle_no = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_dt = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_dt = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=20, blank=True, null=True) 