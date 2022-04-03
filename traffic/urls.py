
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ruun.urls")),


]
admin.site.site_header='SY Traffic Managment'
admin.site.site_title='Sy Traffic'
admin.site.index_title='SY Traffic Site administration'
