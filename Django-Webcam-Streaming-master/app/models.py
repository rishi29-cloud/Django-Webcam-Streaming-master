from django.db import models
import re 

from django.core.exceptions import ValidationError
 
# creating a validator function
def validate_vehicle_no(value):
    pt = "^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
    x = re.search(pt, value)
    print("test________________________________________________-")
    if x:
        return value
    else:
        raise ValidationError("Invalid Vehicle Number Please check")

# Create your models here.
class vehicle(models.Model):
    vehicle_no = models.CharField(max_length=255, blank=True, null=True, validators =[validate_vehicle_no])
    owner = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_dt = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_dt = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=20, blank=True, null=True) 
