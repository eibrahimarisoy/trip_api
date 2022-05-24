from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User


class CustomUserAdmin(UserAdmin):
    """
    ined a custom admin model here to ensure that users created 
    admin panel have their passwords hashed. For this, you need to 
     'UserAdmin' instead of ModelAdmin.
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('status', 'first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_admin', 'is_staff',
                'is_superuser', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'updated_at')}),
        (_('Authentication Info'), {'fields': ('email', 'phone_number',)}),
    )
    readonly_fields = ['username', 'updated_at']
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, CustomUserAdmin)
