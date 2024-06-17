from django.contrib import admin
from .models import StickyNote


class StickyNoteAdmin(admin.ModelAdmin):
    # Display the user field in the admin view
    list_display = ('title', 'user', 'created_at')


admin.site.register(StickyNote, StickyNoteAdmin)
