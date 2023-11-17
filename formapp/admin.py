from django.contrib import admin

# Register your models here.
from .models import provision,Reintegration

admin.site.register(provision)
admin.site.register(Reintegration)