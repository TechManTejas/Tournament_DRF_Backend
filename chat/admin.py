# admin.py
from django.contrib import admin
from .models import ChatSupport, ChatClub

@admin.register(ChatSupport)
class ChatSupportAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'message', 'timestamp')

@admin.register(ChatClub)
class ChatClubAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'message', 'timestamp')
