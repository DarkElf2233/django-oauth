from django.urls import path
from myapp import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('register/', views.UsersRegister.as_view()),

    path('token/', views.ObtainTokenView.as_view()),
    path('token/revoke/', views.RevokeTokenView.as_view()),

    path('books/', views.BooksView.as_view(), name='books'),
]
