from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from ruun.serializers import CarSerializer,DriverSerializer,LicenseSerializer,InsuranceSerializer,ViolationsSerializer
from ruun.models import Driver,Car,License,Insurance,Violations

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDri(request):
    user=request.user
    dri=user.driver_set.all()
    serializer=DriverSerializer(dri,many=True)
    return Response(serializer.data)