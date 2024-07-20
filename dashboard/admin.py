from django.contrib import admin
from .models import *

admin.site.register(Staff_UserAuth)

from django.contrib.admin.models import LogEntry
from django.conf import settings


class CustomLogEntry(LogEntry):
    # Define the user field correctly
    custom_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

admin.site.register(CustomLogEntry)