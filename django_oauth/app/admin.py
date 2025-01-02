from django.contrib import admin
from django.contrib.auth.models import Group
from app.models import User, Book

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    exclude = ['password', 'is_superuser', 'groups', 'last_login', 'user_permissions', 'date_joined']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
