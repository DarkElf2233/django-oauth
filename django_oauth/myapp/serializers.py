from rest_framework.serializers import ModelSerializer
from myapp.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
