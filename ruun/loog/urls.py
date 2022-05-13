from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


"""
    path('ca/',views.getCar),
    path('lac/',views.getlic),
    path('viooo/<str:pk>/',views.getVio),
    path('ran/<str:pk>/',views.getM),
"""


urlpatterns = [
    path('',views.getRoutes ),
    path('driii/',views.getDri),
    path('liic/<int:id>/',views.LicenseRetrieveAPIView.as_view()),
    path('ins/',views.getins),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]