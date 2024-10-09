from django.urls import path
from .views import CategoriesAPIView, FoldersAPIView, AddFoldersAPIView, AddDocumentTypeAPIView



app_name = 'main'

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('folders/<int:pk>/', FoldersAPIView.as_view(), name='folders'),
    path('add-folders/<int:pk>/', AddFoldersAPIView.as_view(), name='add-folders'),
    path('get-doc-type/', AddDocumentTypeAPIView.as_view(), name='get-doc-type'),
]