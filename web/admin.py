from django.contrib import admin
from .models import Blog,Service

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    prepopulated_fields = {"slug": ("name",)}
