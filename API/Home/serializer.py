from rest_framework import serializers
from API.Home.models import HomeModel


class HomeSerializer(serializers.Serializer):
    urls = serializers.CharField(max_length=5000)

    def create(self, validated_data):
        return HomeModel.objects.create(**validated_data)
