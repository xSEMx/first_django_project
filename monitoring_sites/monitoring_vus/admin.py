from django.contrib import admin
from .models import Sites, Comments, Notifications, TelegramLatestMessageIds

@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'status', 'famous')
    list_display_links = ('id', 'url')
    list_editable = ('status', 'famous')
    list_filter = ('status', 'famous')
    search_fields = ('id', 'url')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'evaluation', 'review', 'site')
    list_display_links = ('id', 'user', 'site')
    list_filter = ('user', 'evaluation', 'site')
    search_fields = ('id', 'evaluation', 'review')


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'site')
    list_display_links = ('id', 'email')
    list_filter = ('email', 'site')
    search_fields = ('id',)


@admin.register(TelegramLatestMessageIds)
class TelegramLatestMessageIdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'message_id')
    list_display_links = ('id', 'chat_id')
    search_fields = ('id', 'chat_id')

    
