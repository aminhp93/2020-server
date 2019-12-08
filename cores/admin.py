from django.contrib import admin
from .models import Config

class ConfigAdmin(admin.ModelAdmin):
    model = Config

    list_display = ('id', 'key', 'value', 'description')
    search_fields = ('key',)

admin.site.register(Config, ConfigAdmin)
