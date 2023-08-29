from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ['id','username','role']
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active')}),
    )
admin.site.register(CustomUser,CustomUserAdmin)
