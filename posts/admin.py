from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = ('id', 'title', 'content', 'creator',)
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)
