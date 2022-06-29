from django.contrib import admin

from AppActivity.models import Resource, Folder, Archive, Activity, Quiz, Assigment
# Register your models here.

admin.site.register(Resource)
admin.site.register(Folder)
admin.site.register(Archive)
admin.site.register(Activity)
admin.site.register(Quiz)
admin.site.register(Assigment)
