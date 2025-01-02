import requests
from requests.auth import HTTPBasicAuth
from rest_framework import status, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from app.models import Book
from app.serializers import BookSerializer

import os
from dotenv import load_dotenv

load_dotenv()


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

data = {
    'grant_type': 'password',
    'username': 'admin',
    'password': 'admin'
}

def get_token(request):
    response = requests.post('http://localhost:8000/auth/token/', data=data, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    print(response.json())
    return JsonResponse(response.json())


class BookList(APIView):
    """
    List all books or create a new book.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data)  

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
