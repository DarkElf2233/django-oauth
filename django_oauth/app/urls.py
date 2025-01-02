from django.urls import path
from app import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('token/', views.get_token),
]
