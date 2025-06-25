from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'image', 'short_description')  # fixed 'crated_at'

admin.site.register(Work, WorkAdmin)
