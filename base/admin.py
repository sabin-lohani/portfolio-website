from django.contrib import admin

from .models import SiteSetting, PersonalInfo, Experience, Education

# Register your models here.
admin.site.register(SiteSetting)
admin.site.register(PersonalInfo)
admin.site.register(Experience)
admin.site.register(Education)
