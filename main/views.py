from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Category, Folders, DocumentType, Files
from django.db.models import Q
from .serializers import (CategorySerializer, FoldersSerializer, DocumentTypeSerializer,
                          FilesSerializer, AddFilesSerializer)



class CategoriesAPIView(APIView):
    """
    Bashcha kategoriyalarni olish uchun view
    fields = ['id', 'name', 'created_at']
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({'message': 'Barcha kategoriyalar.....', 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FoldersAPIView(APIView):
    """
    Arxivchi kategoriyaga tegishli papkalrni olish uchun view
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        try:
            folder = Folders.objects.filter(category_id=pk)
            serializer = FoldersSerializer(folder, many=True)
            return Response({'message': "Barcha papkalar.....", 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "Papkalar yaratilmagan", 'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AddFoldersAPIView(APIView):
    """
    Bo'lim kategoriyalariga papkalr yaratish uchun view
    fields = ['id', 'category', 'number', 'name', 'created_at']
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({'message': "Bu id da kategoriya topilmadi....."}, status=status.HTTP_404_NOT_FOUND)

        folders_data = request.data.get('folders')
        if not folders_data:
            return Response({"error": "Papka yaratish talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)

        for folders in folders_data:
            folders['category'] = category.id
            serializer = FoldersSerializer(data=folders)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Papka muvaffaqiyatli qo‘shildi.", 'data': serializer.data},
                        status=status.HTTP_201_CREATED)


class AddDocumentTypeAPIView(APIView):
    """
    Hujjat turlarini olish uchun view
    fields = ['id', 'name']
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        doc_type = DocumentType.objects.all()
        serializer = DocumentTypeSerializer(doc_type, many=True)
        return Response({'message': 'Barcha hujjat turlari..', 'data': serializer.data},
                        status=status.HTTP_200_OK)


class GetFilesAPIView(APIView):
    """
    Papkaya tegishli fayllarni olish uchun view
    fields = ['id', 'file_code', 'created_at']
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        try:
            file = Files.objects.filter(folder_id=pk)
            serializer = FilesSerializer(file, many=True)
            return Response({'message': 'Barcha Fayllar.....', 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AddFilesAPIView(APIView):
    """
    Arxiv fayllarini yuklash uchun view
    fields = ['id', 'folder', 'document', 'file_code', 'file']
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        serializer = AddFilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Malumot yuklandi.....', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Malumot yulashda xatoli yuzberdi", 'data': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class SearchFilesAPIView(APIView):
    """
    Malumotlarni Papka id Hujjat id va fayllar kodi bilan izlash uchun views
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        folder_id = request.query_params.get('folder_id')
        file_code = request.query_params.get('file_code', None)

        if not folder_id:
            return Response({"message": "Folder ID va Document ID kiritilishi kerak"}, status=status.HTTP_400_BAD_REQUEST)

        files = Files.objects.filter(folder_id=folder_id)

        # Agar file_code qidirilayotgan bo'lsa, uni ham qo'shish mumkin
        if file_code:
            files = files.filter(Q(file_code__icontains=file_code))

        if files.exists():
            serializer = FilesSerializer(files, many=True)
            return Response({'message': "Siz izlagan malumot", 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Hech qanday fayl topilmadi"}, status=status.HTTP_404_NOT_FOUND)


class SearchFoldersAPIView(APIView):
    """
    Kategoriyaga tegishli Papkalarni izlash uchun views
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        number = request.query_params.get('number', '')
        name = request.query_params.get('name', '')

        if not category_id:
            return Response({"message": "Kategory id kiritilishi kerak"},
                            status=status.HTTP_400_BAD_REQUEST)
        folders = Folders.objects.filter(category_id=category_id)
        if number or name:
            folders = folders.filter(Q(number__icontains=number) | Q(name__icontains=name))
        if folders.exists():
            serializer = FoldersSerializer(folders, many=True)
            return Response({'message': "Siz izlagan malumot", 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Hech qanday fayl topilmadi"}, status=status.HTTP_404_NOT_FOUND)
