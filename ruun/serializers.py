

from .models import Driver,Car,License,Insurance,Violations
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):


    class Meta:
       model = Car
       fields = ['plate', 'brand', 'modeel', 'weight','cs','cd','fueltype','fueltankcapacity','pyy','rd','en','cn',
                'color','transmissiontype','nog','maxspeed','enginedisplacement','violnum','driver']

class ViolationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
       model=Violations
       fields=['typeofv','datev','fee','vionum','plate']











class LicenseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
       model=License
       fields = ['namee','Bpay','nationalitty','nationalnuum','bloadtype','licensenum','red','fd','city','typeoflicense','driver']



class InsuranceSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
       model=Insurance
       fields=['typeofi','noi','dateofrenewal','dateofexpired','renewalfee','plate']



class ViolationsSerializer(serializers.HyperlinkedModelSerializer):

    
    class Meta:
       model=Violations
       fields=['typeofv','datev','fee','vionum','plate']



class DriverSerializer(serializers.HyperlinkedModelSerializer):
    depth=1
    
    class Meta:
     model = Driver
     fields = ['name', 'code','baalance', 'bd','sex','nationality','nationalnum','carnum','photo']

