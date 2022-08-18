from django.contrib import admin
from services.models import User
from services.models import Pet
from services.models import Volunteer
from services.models import Adoption
from services.models import Feedback 
# Register your models here.

class User_Admin(admin.ModelAdmin):
    list_display=('fnm','lnm','unm','email','pno','password','role','date')
admin.site.register(User,User_Admin) 

class Pet_Admin(admin.ModelAdmin):
    list_display=('name','breed','color','age','size','weight','gender','image','addedby','date')
admin.site.register(Pet,Pet_Admin)

class Volunteer_Admin(admin.ModelAdmin):
    list_display=('fnm','lnm','unm','email','pno','address','date')
admin.site.register(Volunteer,Volunteer_Admin)

class Adoption_Admin(admin.ModelAdmin):
    list_display=('unm','pid','email','pno','address','date','approve')
admin.site.register(Adoption,Adoption_Admin)

class Feedback_Admin(admin.ModelAdmin):
    list_display=('name','email','message','date','enable')
admin.site.register(Feedback,Feedback_Admin)