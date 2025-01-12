from rest_framework.serializers import ModelSerializer
from myapp.models import Book, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
