from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Trainers)
admin.site.register(Courses)
admin.site.register(ClassStatus)
admin.site.register(ClassName)

admin.site.register(StudentsEnroll)