from django.contrib import admin
from myapp.models import Book, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'created', 'is_staff']
    exclude = ['username', 'first_name', 'last_name', 'password', 'groups', 'last_login', 'user_permissions', 'date_joined']
