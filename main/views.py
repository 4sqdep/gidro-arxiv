from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer



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