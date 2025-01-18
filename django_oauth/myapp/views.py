from django.utils import timezone
from django.http import Http404, JsonResponse
from django.contrib.auth.hashers import make_password
from oauth2_provider.models import AccessToken, RefreshToken
from oauth2_provider.views import TokenView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.models import Book, User
from myapp.serializers import BookSerializer, UserSerializer


class UsersRegister(APIView):
    """
    Create a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        ### Add validation if needed

        # Validata username
        # is_valid = validate_username(request.data['username'])
        # if is_valid != True:
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Validate password
        # is_valid = validate_password(request.data['password'])
        # if is_valid != True:
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Hashing password
        request.data['password'] = make_password(request.data['password'])

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersList(APIView):
    """
    List all users.
    """
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]

    def get(self, request, format=None):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)  


class UserDetail(APIView):
    """
    Retrieve, update or delete a user.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObtainTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({
                "error": "invalid_user",
                "error_description": "User does not exists",
            }, status=status.HTTP_400_BAD_REQUEST)

        AccessToken.objects.filter(user_id=user.id, expires__lt=timezone.now()).delete()
        RefreshToken.objects.filter(access_token_id__isnull=True).delete()

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

        request.POST = request.POST.copy()
        request.POST['username'] = user.email

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
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

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
