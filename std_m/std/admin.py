from django.contrib import admin
from .models import Student_info

# Register your models here.
class Student_info_Admin(admin.ModelAdmin):
    list_display = [
        'roll', 'full_name', 'image','department','email','address','phone'
    ]
admin.site.register(Student_info)