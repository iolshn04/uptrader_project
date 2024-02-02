from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "url"
    list_display_links = ("pk",)
