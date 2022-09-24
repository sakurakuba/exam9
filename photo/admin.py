from django.contrib import admin
from photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'created_at')
    list_display_links = ('pk', 'title')
    list_filter = ('created_at',)
    search_fields = ('title',)


admin.site.register(Photo, PhotoAdmin)
