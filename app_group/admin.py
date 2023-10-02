from django.contrib import admin
from .models import GroupChat, Message

@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = 'id', 'sender', 'group', 'created_date'
    list_display_links = 'group'
    list_per_page = 10
    ordering = '-id',
