from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'permalink', 'url', 'is_visible',)
    list_filter = ('is_visible',)
    search_fields = ('title',)
