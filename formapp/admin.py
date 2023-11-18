from django.contrib import admin

# Register your models here.
from .models import provision,Reintegration,AwarenessEvent,MasterRecord, StaffAttendence,NightSurvey,FoodMenu,SalaryRegister

admin.site.register(provision)
admin.site.register(Reintegration)
admin.site.register(StaffAttendence)
admin.site.register(NightSurvey)
admin.site.register(AwarenessEvent)
admin.site.register(FoodMenu)
admin.site.register(SalaryRegister)
admin.site.register(MasterRecord)