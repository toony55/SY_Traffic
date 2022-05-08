from django.contrib import auth
from django.db import models


class Driver(models.Model):
   """The drivers Info."""
   name = models.CharField(max_length=50,help_text="The name of the driver.")
   code = models.CharField(max_length=50,help_text="The Secret Code.")
   baalance = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
   bd = models.DateField(verbose_name="birth date")
   sex = models.CharField(max_length=6)
   nationality = models.CharField(max_length=30, default="")
   nationalnum = models.CharField(max_length=30, default="")
   carnum = models.CharField(max_length=30, default="",verbose_name="The Number of Cars Owned By The Driver")
   photo=models.URLField(max_length = 200,default="")


class Car(models.Model):
   """The Cars Info."""
   plate = models.CharField(max_length=30,unique=True)
   brand = models.CharField(max_length=40,verbose_name="The brand of the car.", default="")
   modeel = models.CharField(max_length=40,verbose_name="The model of the car.")
   weight = models.CharField(help_text="Weight of the Car.",max_length=30)
   cs = models.CharField(verbose_name="Car Seats",default="",max_length=30)
   cd = models.CharField(verbose_name="Car Doors", default='',max_length=30)
   fueltype = models.CharField(max_length=30, default="")
   fueltankcapacity = models.CharField(max_length=30, default="")
   pyy = models.CharField(help_text="Production Year", default='',max_length=30)
   rd = models.DateField(verbose_name="registration date", default="")
   en = models.CharField(help_text="Engine Number",unique=True,max_length=30, default="")
   cn = models.CharField(verbose_name="Chassis Number",max_length=30, default="")
   color = models.CharField(max_length=30, default="")
   transmissiontype= models.CharField(max_length=30, default="")
   nog = models.CharField(help_text='Number Of Gears', default='',max_length=30)
   maxspeed= models.CharField(max_length=30, default="")
   enginedisplacement= models.CharField(max_length=30, default="")
   driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
   violnum = models.CharField(max_length=30, default="")




class License(models.Model):
   """The License Info."""
   namee= models.CharField(max_length=30, default="")
   Bpay= models.CharField(max_length=30, default="",help_text="Born Place and Year")
   nationalitty = models.CharField(max_length=30, default="")
   nationalnuum = models.CharField(max_length=30, default="")
   bloadtype= models.CharField(max_length=30, default="")
   licensenum= models.CharField(max_length=30, default="")
   red = models.DateField(help_text="registration Date", default="")
   fd = models.DateField(help_text="finished Date", default="")
   city= models.CharField(max_length=30, default="")
   typeoflicense= models.CharField(max_length=30, default="")
   code = models.ForeignKey(Driver,on_delete=models.CASCADE)



class Violations(models.Model):
   """The Cars Violations ."""
   typeofv = models.CharField(max_length=50,help_text="Type Of Violations.",default="")
   datev = models.DateField(verbose_name="Violation date", default="")
   fee = models.DecimalField(max_digits=10,decimal_places=2, default="")
   plate = models.ForeignKey(Car,on_delete=models.CASCADE)
   vionum = models.CharField(max_length=30, default="")



class Insurance(models.Model):
   """The Cars Insurance ."""
   typeofi = models.CharField(max_length=50,help_text="Type Of Insurance.", default="")
   noi = models.CharField(help_text='Number Of Insurance', default='',max_length=30)
   dateofrenewal = models.DateField(verbose_name="Renewal date", default="")
   dateofexpired = models.DateField(verbose_name="Experation date", default="")
   renewalfee = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
   plate = models.ForeignKey(Car,on_delete=models.CASCADE)


