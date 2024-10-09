from rest_framework import serializers
from .models import Category, Folders, DocumentType



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
