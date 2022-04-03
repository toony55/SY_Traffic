
from django.urls import include, path
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register(r'carrs', CarViewSet)
router.register(r'lic',LicenseViewSet)
router.register(r'ins',InsuranceViewSet)
router.register(r'vio',ViolationseViewSet)
router.register(r'dri',DriverViewSet)
router.register(r'bal',BalanceViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
