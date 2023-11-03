from django.contrib import admin

# Register models here
from . import models


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at", "id", "status"]
    search_fields = ["title", "content", "id"]
    list_filter = ["published_at", "status"]
    list_per_page = 10
    list_editable = ["status"]


admin.site.register(models.Articles, ArticlesAdmin)
admin.site.register(models.Categories)
admin.site.register(models.Tags)
