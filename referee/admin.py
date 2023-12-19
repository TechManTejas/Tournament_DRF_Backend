from django.contrib import admin
from .models import Referee

@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ('name', 'club')
