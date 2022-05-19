from django.contrib import admin

from AppUser.models import customUser, Teacher, Parent, Annotation, EnrollmentSubject, EnrollmentCourse
# Register your models here.

admin.site.register(customUser)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Annotation)
admin.site.register(EnrollmentSubject)
admin.site.register(EnrollmentCourse)
