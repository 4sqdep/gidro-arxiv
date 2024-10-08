from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from .models import Category, Folders
from .serializers import CategorySerializer, FoldersSerializer



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

    def get(self, request, pk=None):
        try:
            folder = Folders.objects.filter(id=pk).first()
            serializer = FoldersSerializer(folder, many=True)
            return Response({'message': "Barcha papkalar.....", 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "Papkalar yaratilmagan", 'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
