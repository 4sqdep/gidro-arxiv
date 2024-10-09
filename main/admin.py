from django.contrib import admin
from .models import Category, Folders, DocumentType



class FoldersInline(admin.TabularInline):
    model = Folders
    extra = 1
    fields = ['id', 'name', 'number', 'created_at']
    readonly_fields = ['created_at']



class CategoryAdmin(admin.ModelAdmin):
    inlines = [FoldersInline]
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']


admin.site.register(DocumentType, DocumentTypeAdmin)

