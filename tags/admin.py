from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    model = Tag

    list_display = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
