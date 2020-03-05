from django.contrib import admin
from .models import student,teacher
#creating admin models for normal models
class Adminstudent(admin.ModelAdmin):
    list_display = ['name','email','address','rollno','marks']
class Adminteacher(admin.ModelAdmin):
    list_display = ['name','email','address','subject','salary']


# Register your models here.
admin.site.register(student,Adminstudent)
admin.site.register(teacher,Adminteacher)
