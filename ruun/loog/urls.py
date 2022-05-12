from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)





urlpatterns = [
    path('',views.getRoutes ),
    path('driii/',views.getDri),
    path('viooo/<str:pk>/',views.getVio),
    path('liic/<int:id>/',views.LicenseRetrieveAPIView.as_view()),
    path('ins/',views.getins),
    path('ran/<str:pk>/',views.getM),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]