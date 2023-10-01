from django.contrib import admin
from .models import Groups

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = 'id', 'group', 'slug',
    list_display_links = 'group',
    search_fields = 'id', 'group', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('group',),
    }
