from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from ruun.serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer,mmmSerializer
from ruun.models import Driver,Car,License,Insurance,Violations,mmm
from rest_framework import generics, permissions

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

#red this issssss Vioooooolations APi

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getVio(request,pk):
    user=request.user
    vio=Violations.objects.get(id=pk)
    serializer=ViolationsSerializer(vio,many=False)
    return Response(serializer.data)

#red this issssss Liiiiiiiicense APi

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getlic(request):
    user=request.user
    driver=Driver.objects.get(user=user)
    lic=driver.License_set.all()
    serializer=LicenseSerializer(lic,many=True)
    return Response(serializer.data) 


#red this issssss teeeeeeeeest APi
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getM(request,pk):
    user=request.user
    dri=user.mmm_set.get(id=pk)
    serializer=mmmSerializer(dri,many=False)
    return Response(serializer.data)

#red this issssss Innnnnnnsurance APi

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getins(request):
    user=request.user
    ins=user.Insurance_set.get()
    serializer=LicenseSerializer(ins,many=True)
    return Response(serializer.data) 


#red this issssss Liiiiiiiicense APi

class LicenseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    
    def retrieve(self, request, id):
        license = self.get_queryset().filter(id=id)
        serializer = self.serializer_class(license)
        return Response(serializer.data)
    