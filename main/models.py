from django.db import models
from account.models import User




class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategoriya nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kategoriya kiritilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Folders(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    number = models.CharField(max_length=25, verbose_name="Papka nomeri")
    name = models.CharField(max_length=500, verbose_name="Papka nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Papka kiritilgan vaqti")

    def __str__(self):
        return f"{self.category} -- {self.name}"

    class Meta:
        verbose_name = "Papka"
        verbose_name_plural = "Papakalar"