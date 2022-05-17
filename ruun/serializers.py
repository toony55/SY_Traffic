

from .models import Driver,Car,License,Insurance,Violations,mmm
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):


    class Meta:
       model = Car
       fields = ['plate', 'brand', 'modeel', 'weight','cs','cd','fueltype','fueltankcapacity','pyy','rd','en','cn',
                'color','transmissiontype','nog','maxspeed','enginedisplacement','violnum','driver']

class ViolationsSerializer(serializers.ModelSerializer):

    class Meta:
       model=Violations
       fields='__all__'




class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
       model=License
       fields ="__all__"



class InsuranceSerializer(serializers.ModelSerializer):


    class Meta:
       model=Insurance
       fields=['typeofi','noi','dateofrenewal','dateofexpired','renewalfee','plate']



class ViolationsSerializer(serializers.ModelSerializer):

    
    class Meta:
       model=Violations
       fields=['typeofv','datev','fee','vionum','plate','IsPaid']

class mmmSerializer(serializers.ModelSerializer):

    
    class Meta:
       model=mmm
       fields='__all__'

class DriverSerializer(serializers.ModelSerializer):
    depth=1
    
    class Meta:
     model = Driver
     fields = ['name', 'code','baalance', 'bd','sex','nationality','nationalnum','carnum','photo']



