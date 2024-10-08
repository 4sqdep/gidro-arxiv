from django.db import models
from account.models import User




class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategoriya nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kategoriya kiritilgan vaqti")

    def __str__(self):
        return self.name
