from django.contrib import admin
from ruun.models import Driver,Car,License,Insurance,Violations,mmm



class CarAdmin(admin.ModelAdmin):
    list_display=('plate','brand','modeel')
    date_hierarchy='rd'
    list_filter=('brand','rd')
    search_fields=('brand','rd','driver__name')

class DriverAdmin(admin.ModelAdmin):
    list_display=('name','code')
    date_hierarchy='bd'
    list_filter=('name','bd')

class InsuranceAdmin(admin.ModelAdmin):
    list_display=('typeofi','renewalfee')


class LicenseAdmin(admin.ModelAdmin):
    list_display=('namee','Bpay')

class ViolationsAdmin(admin.ModelAdmin):
    list_display=('typeofv','fee')


class mmmAdmin(admin.ModelAdmin):
    list_display=('cc','nn')
   

# Register your models here.
admin.site.register(Driver,DriverAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(mmm,mmmAdmin)
admin.site.register(License,LicenseAdmin)
admin.site.register(Insurance,InsuranceAdmin)
admin.site.register(Violations,ViolationsAdmin)
