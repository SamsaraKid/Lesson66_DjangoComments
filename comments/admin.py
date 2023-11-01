from django.contrib import admin
from .models import *


class Comadmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'timedate']


admin.site.register(Comment, Comadmin)