from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from .serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer
from .models import Driver,Car,License,Insurance,Violations
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Driver,Car,License,Insurance,Violations
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions



from rest_framework.authentication import  TokenAuthentication
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.settings import  api_settings

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = InsuranceSerializer



class ViolationseViewSet(viewsets.ModelViewSet):
    queryset = Violations.objects.all()
    serializer_class = ViolationsSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    http_method_names = ['get','post','retrieve','put','patch']

"""class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES"""

         