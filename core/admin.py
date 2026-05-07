from django.contrib import admin
from .models import Hack

@admin.register(Hack)
class HackAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description',)