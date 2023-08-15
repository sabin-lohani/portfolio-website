from django.contrib import admin

from .models import SiteSetting, PersonalInfo, Experience, Education, Testimonial, Award, NavLink, FaIcon, SocialLink
# Register your models here.
admin.site.register(SiteSetting)
admin.site.register(PersonalInfo)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Testimonial)
admin.site.register(Award)
admin.site.register(NavLink)
admin.site.register(FaIcon)
admin.site.register(SocialLink)