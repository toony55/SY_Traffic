from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from .serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer
from .models import Driver,Car,License,Insurance,Violations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class ViolationseViewSet(viewsets.ModelViewSet):
    queryset = Violations.objects.all()
    serializer_class = ViolationsSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    http_method_names = ['get','post','retrieve','put','patch']



"""
@api_view(['GET','POST'])
def lic_list(request):
    if request.method == 'GET':
       liist=Balance.objects.all()
       serializer = BalanceSerializer(liist,many=True)
       return Response(serializer.data)

    elif request.method == 'POST':
         serializer = BalanceSerializer(data=request.data,read_only=True)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         """
         


