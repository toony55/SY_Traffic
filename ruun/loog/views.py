from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from ruun.serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer,mmmSerializer
from ruun.models import Driver,Car,License,Insurance,Violations,mmm
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/loog/token',
        '/loog/token/refresh'
    ]
    return Response(routes)



#red this issssss Drrrrrrrrrrrrrrrriver APi


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDri(request):
    user=request.user
    dri=user.driver_set.all()
    serializer=DriverSerializer(dri,many=True)
    return Response(serializer.data)


#red this issssss Innnnnnnsurance APi

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def getins(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver.id)
    serlist=[]
    for car in cars:
      ins = Insurance.objects.filter(plate=car.id)
      serializer=InsuranceSerializer(ins,many=True)
      serlist.append(serializer.data)
    return Response(serlist) 


#red this issssss Vioooooolations APi
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def getvio(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver.id)
    serlist=[]
    for car in cars:
      vio= Violations.objects.filter(plate=car.id)
      serializer=ViolationsSerializer(vio,many=True)
      serlist.append(serializer.data)
    return Response(serlist) 
      
#red this issssss Liiiiiiiicense APi

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def getlic(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    lic = License.objects.filter(driver=driver.id)
    serializer=LicenseSerializer(lic,many=True)
    return Response(serializer.data)



    
#red this issssss Caaaaaaaarrrrr APi

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def getCar(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver.id)
    serializer=CarSerializer(cars,many=True)
    return Response(serializer.data) 








    