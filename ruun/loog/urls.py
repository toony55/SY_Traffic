from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('',views.getRoutes ),
    path('driver/',views.getDri),
    path('violation/',views.getvio),
    path('pay/<int:vionum>/',views.getOneVio),
    path('renew/<int:noi>/',views.getRenew),
    path('license/',views.getlic),
    path('cars/',views.getCar),
    path('inss/',views.getins),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]