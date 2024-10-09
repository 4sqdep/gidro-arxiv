from django.contrib import admin
from .models import Category, Folders



class FoldersInline(admin.TabularInline):
    model = Folders
    extra = 1
    fields = ['id', 'name', 'number', 'created_at']
    readonly_fields = ['created_at']



class CategoryAdmin(admin.ModelAdmin):
    inlines = [FoldersInline]
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)

