from django.contrib import admin
from core.models import FSUser
from django.contrib.sessions.models import Session


class FSUserAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Status', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'last_login')
        }),
        ('Groups & Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')
        }),
    )
    list_display = ('email', 'is_staff', 'last_login')
    search_fields = ['email']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login')
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(FSUser, FSUserAdmin)
admin.site.register(Session)
