
from django.urls import include, path,re_path
from rest_framework import routers
from .views import *
from django.views.static import serve
from django.conf import settings




router = routers.DefaultRouter()
router.register('carrs', CarViewSet)
"""router.register(r'lic',LicenseViewSet)
router.register(r'ins',InsuranceViewSet)
router.register(r'vio',ViolationseViewSet)
router.register(r'dri',DriverViewSet)
router.register(r'bal',BalanceViewSet)"""


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
