from django.contrib import admin

from feeds.models import Feed

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active')
    list_editable = ('url', 'is_active')
admin.site.register(Feed, FeedAdmin)
