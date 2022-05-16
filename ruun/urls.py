
from django.urls import include, path,re_path
from rest_framework import routers
from .views import *
from django.views.static import serve
from django.conf import settings
from . import views





router = routers.DefaultRouter()
router.register(r'ca',CarViewSet)
router.register(r'inc',InsuranceViewSet)
router.register(r'lic',LicenseViewSet)
router.register(r'vio',ViolationseViewSet)
router.register(r'dri',DriverViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('pay',views.Pay.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

