from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class LoggedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({})
