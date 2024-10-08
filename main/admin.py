from django.contrib import admin
from .models import Category, Folders



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class FoldersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'created_at']
    list_display_links = ['name', 'number']
    search_fields = ['name', 'number']


admin.site.register(Folders, FoldersAdmin)
