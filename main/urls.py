from django.urls import path
from .views import CategoriesAPIView, FoldersAPIView



app_name = 'main'

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('folders/<int:pk>/', FoldersAPIView.as_view(), name='folders'),
]