from rest_framework import serializers
from .models import Category



class CategorySerializer(serializers.ModelSerializer):
    """Barcha kategoriyalarni olish uchun"""
    class Meta:
        model = Category
        fields = ['id', 'name']


