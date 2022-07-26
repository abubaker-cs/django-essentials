from django.contrib import admin

from . import models


class NotesAdmin(admin.ModelAdmin):
    # list_display will update the label in the dashboard
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
