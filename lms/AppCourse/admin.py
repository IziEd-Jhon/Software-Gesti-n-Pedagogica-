from django.contrib import admin

# Register your models here.
from AppCourse.models import Course, Subject, Section
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('verbose','code',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(Section)
