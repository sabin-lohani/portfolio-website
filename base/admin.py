from django.contrib import admin

from .models import SiteSetting, PersonalInfo

# Register your models here.
admin.site.register(SiteSetting)
admin.site.register(PersonalInfo)
