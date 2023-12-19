from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'message', 'verified')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('role', 'verified')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'message', 'verified')}),
    )

admin.site.register(User, CustomUserAdmin)