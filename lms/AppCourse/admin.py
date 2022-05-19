from django.contrib import admin

# Register your models here.
from AppCourse.models import Course, Subject, Section
# Register your models here.

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Section)
