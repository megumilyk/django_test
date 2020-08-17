from django.contrib import admin
from .models import *
# Register your models here.

class StuAdmin(admin.ModelAdmin):
    list_display = ('fname',)

admin.site.register(Stu,StuAdmin)