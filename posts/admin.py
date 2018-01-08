from django.contrib import admin
from .models import Post
# Register your models here.
#
# @admin.register(admin.ModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'updated')
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp', 'title']
    list_editable = ['title']
    search_fields = ['title', 'content']
    ordering = ['updated']
    class Meta:
        model = 'Post'

admin.site.register(Post, PostModelAdmin)
