from django.contrib import admin

from .models import BotConfig, BotUsers


@admin.register(BotConfig)
class BotConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'token', 'server_url', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', "first_name", "last_name", 'is_bot')
    list_display_links = ('user_id',)
    search_fields = ('user_id', 'user_name', "first_name", "last_name", 'is_bot')

    def has_delete_permission(self, request, obj=None):
        return True
