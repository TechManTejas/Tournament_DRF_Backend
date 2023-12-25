from django.contrib import admin
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'tournament', 'round')
    search_fields = ['name']

admin.site.register(Group, GroupAdmin)
