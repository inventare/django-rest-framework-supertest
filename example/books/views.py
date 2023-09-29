from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers

class DemoSerializer(serializers.Serializer):
    email = serializers.EmailField()

class LoggedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({})
    
    def post(self, request):
        serializer = DemoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response({})
