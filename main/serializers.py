from rest_framework import serializers
from .models import Category, Folders, DocumentType, Files



class CategorySerializer(serializers.ModelSerializer):
    """Barcha kategoriyalarni olish uchun"""
    class Meta:
        model = Category
        fields = ['id', 'name']



class FoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folders
        fields = ['id', 'category', 'number', 'name']


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name']


class FilesSerializer(serializers.ModelSerializer):
    """
    Fayllarni olish uchun serializers
    """
    class Meta:
        model = Files
        fields = ['id', 'file_code', 'file', 'created_at']


class AddFilesSerializer(serializers.ModelSerializer):
    """
    Arxivga fayllarni yuklash uchun serializers
    """
    class Meta:
        model = Files
        fields = ['id', 'folder', 'document', 'calendar', 'file_code', 'file', 'created_at']
