from django.contrib import admin

from AppUser.models import customUser, Teacher, Parent
# Register your models here.

admin.site.register(customUser)
admin.site.register(Teacher)
admin.site.register(Parent)