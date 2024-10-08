from django.urls import path
from .views import CategoriesAPIView



app_name = 'main'

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
]