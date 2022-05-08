

from .models import Driver,Car,License,Insurance,Violations
from rest_framework import serializers


class DriverSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
     model = Driver
     fields = ['name', 'code','baalance', 'bd','sex','nationality','nationalnum','carnum','photo']



class CarSerializer(serializers.ModelSerializer):

    driver = DriverSerializer()

    class Meta:
       model = Car
       fields = ['plate', 'brand', 'modeel', 'weight','cs','cd','fueltype','fueltankcapacity','pyy','rd','en','cn',
                'color','transmissiontype','nog','maxspeed','enginedisplacement','violnum','driver']



class LicenseSerializer(serializers.HyperlinkedModelSerializer):

    code=DriverSerializer()
    class Meta:
       model=License
       fields = ['namee','Bpay','nationalitty','nationalnuum','bloadtype','licensenum','red','fd','city','typeoflicense','code']



class InsuranceSerializer(serializers.HyperlinkedModelSerializer):

    plate=CarSerializer()
    class Meta:
       model=Insurance
       fields=['typeofi','noi','dateofrenewal','dateofexpired','renewalfee','plate']



class ViolationsSerializer(serializers.HyperlinkedModelSerializer):

    plate=CarSerializer()
    class Meta:
       model=Violations
       fields=['typeofv','datev','fee','vionum','plate']

