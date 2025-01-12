from django.contrib import admin
from myapp.models import Book, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'created', 'is_staff']
    exclude = ['password', 'groups', 'last_login', 'user_permissions', 'date_joined']
