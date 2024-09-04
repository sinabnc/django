from django.contrib import admin
from .models import Article,Service

@admin.register(Article)
class ArticaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'meta_title','meta_description')
admin.site.register(Service)
