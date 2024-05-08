# admin.py
from django.contrib import admin
from .models import User  

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] 
    
admin.site.register(User, UserAdmin)
