from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from oauth2_provider.views import TokenView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.models import Book
from myapp.serializers import BookSerializer


class ObtainTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({
                "error": "invalid_user",
                "error_description": "User does not exists",
            }, status=status.HTTP_400_BAD_REQUEST)

        active_token = AccessToken.objects.filter(
            user_id=user.id,
            expires__gt=timezone.now()
        )

        if active_token.exists():
            active_token = active_token.first()
            return JsonResponse({
                "access_token": active_token.token,
                "expires_in": (active_token.expires - timezone.now()).total_seconds(),
                "token_type": "Bearer",
                "scope": active_token.scope,
            })

        return super().post(request, *args, **kwargs)


class RevokeTokenView(APIView):
    def post(self, request):
        user_id = request.data['user_id']

        try:
            access_token = AccessToken.objects.get(user_id=user_id, expires__gt=timezone.now())
        except AccessToken.DoesNotExist:
            return Response({"detail": "User does not have access token"}, status=status.HTTP_400_BAD_REQUEST)

        access_token.delete()
        return Response({"detail": "Successfully deleted user credentials"}, status=status.HTTP_200_OK)


class BooksView(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request):
        books = Book.objects.all()
        books_serialzer = BookSerializer(books, many=True)
        return Response(books_serialzer.data)
    
    def post(self, request):
        book_serializer = BookSerializer(request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
