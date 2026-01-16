from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email','username','role','is_staff','is_superuser','is_active','email_verified')
    list_filter = ('role','is_staff','is_superuser','is_active','email_verified')
    search_fields = ('email','username')
    ordering = ('email',)

    fieldsets = (
        (None,{'fields' : ('email','username','password')}),
        ('permissions',{'fields' : ('role','is_staff','is_superuser','is_active','email_verified','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',), 
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_staff', 'is_superuser', 'is_active', 'email_verified'),
        }),
    )

admin.site.register(User,UserAdmin)