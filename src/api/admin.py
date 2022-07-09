from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ('id', 'email', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.register(User, UserAdmin)


