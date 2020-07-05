from rest_framework.response import Response
from rest_framework.views import APIView

from API.Home.serializer import HomeSerializer
from .models import HomeModel
from rest_framework import viewsets, status


# class HomeViewSet(viewsets.ModelViewSet):
#     queryset = HomeModel.objects.all()
#     serializer_class = HomeSerializer

class HomeView(APIView):
    def post(self, request, format=None):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)