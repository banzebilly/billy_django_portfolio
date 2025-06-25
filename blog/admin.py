from django.contrib import admin
from .models import BlogProject

class BlogProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'image', 'short_description')  # fixed 'crated_at'

admin.site.register(BlogProject, BlogProjectAdmin)
