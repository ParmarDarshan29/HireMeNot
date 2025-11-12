from django.contrib import admin
from .models import Roast


@admin.register(Roast)
class RoastAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'upvotes', 'resume_preview')
    list_filter = ('timestamp',)
    search_fields = ('resume_text', 'roast_text')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    
    def resume_preview(self, obj):
        return obj.resume_text[:50] + "..." if len(obj.resume_text) > 50 else obj.resume_text
    resume_preview.short_description = "Resume Preview"

