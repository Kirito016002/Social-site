from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from main import models
from . import serializers


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = models.User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            user = models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UserRelationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = models.UserReletion(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            user_r = models.UserReletion.objects.get(pk=pk)
        except models.UserReletion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        try:
            instance = models.Chat.objects.get(pk=pk)
        except models.Chat.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ChatSerializer(instance)
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        try:
            chat = models.Chat.objects.get(pk=pk)
        except models.Chat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class MassageAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.MassageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            massage = models.Message.objects.get(pk=pk)
        except models.Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.MassageSerializer(massage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            massage = models.Message.objects.get(pk=pk)
        except models.Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        massage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)