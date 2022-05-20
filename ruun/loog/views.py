from itertools import count
from pickle import FALSE
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from ruun.serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer,mmmSerializer
from ruun.models import Driver,Car,License,Insurance,Violations,mmm
from rest_framework import generics, permissions
from .permissions import IsDriver
from rest_framework import status

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
@permission_classes([IsAuthenticated&IsDriver])
def getins(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver.id)
    serlist=[]
    for car in cars:
      ins = Insurance.objects.filter(plate=car.id,IsPaid=False)
      serializer=InsuranceSerializer(ins,many=True)
      serlist.append(serializer.data)
    return Response(serlist) 



#red this issssss Liiiiiiiicense APi

@api_view(['GET'])
@permission_classes([IsAuthenticated&IsDriver])
def getlic(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    lic = License.objects.filter(driver=driver.id)
    serializer=LicenseSerializer(lic,many=True)
    return Response(serializer.data)



    
#red this issssss Caaaaaaaarrrrr APi

@api_view(['GET'])
@permission_classes([IsAuthenticated&IsDriver])
def getCar(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver.id)
    serializer=CarSerializer(cars,many=True)
    return Response(serializer.data) 
    


#red this issssss Vioooooolations APi
@api_view(['GET'])
@permission_classes([IsAuthenticated&IsDriver])
def getvio(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    cars=Car.objects.filter(driver=driver)
    serlist=[]
    for car in cars:
      vio= Violations.objects.filter(plate=car.id,IsPaid=False)
      serializer=ViolationsSerializer(vio,many=True)
      serlist.append(serializer.data)
    return Response(serlist) 
      



#red this issssss the Pay APi
@api_view(['POST'])
@permission_classes([IsAuthenticated&IsDriver])
def getOneVio(request,vionum):
   vio=Violations.objects.get(vionum=vionum)
   driver=Driver.objects.get(id=vio.plate.driver.id)
   if (vio.IsPaid==False):
      if driver.baalance >= vio.fee:
          driver.baalance=driver.baalance - vio.fee
          vio.IsPaid=True
          driver.save()
          vio.save()
          return  Response({"msg": "The fee has been paid successfully.", "is_paid": vio.IsPaid}, status=status.HTTP_200_OK)
      else: 
          vio.IsPaid=False
          vio.save()
          return  Response({"msg": "There is no enough Balance.", "is_paid": vio.IsPaid}, status=status.HTTP_400_BAD_REQUEST)
   else:
       return  Response({"msg": "This Violation has already been Paid"}, status=status.HTTP_400_BAD_REQUEST)




#red this issssss the Renew APi
@api_view(['POST'])
@permission_classes([IsAuthenticated&IsDriver])
def getRenew(request,noi):
   ins=Insurance.objects.get(noi=noi)
   driver=Driver.objects.get(id=ins.plate.driver.id)
   if (ins.IsPaid==False):
      if driver.baalance >= ins.renewalfee:
          driver.baalance=driver.baalance - ins.renewalfee
          ins.IsPaid=True
          driver.save()
          ins.save()
          return  Response({"msg": "Your Insuranve has been Renewed successfully.", "is_paid": ins.IsPaid}, status=status.HTTP_200_OK)
      else: 
          ins.IsPaid=False
          ins.save()
          return  Response({"msg": "There is no enough Balance.", "is_paid": ins.IsPaid}, status=status.HTTP_400_BAD_REQUEST)
   else:
       return  Response({"msg": "Your Insurance has already been Renewed"}, status=status.HTTP_400_BAD_REQUEST)