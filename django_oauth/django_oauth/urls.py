from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adfsdhehtyxqzczq/', admin.site.urls),
    path('api/', include('myapp.urls')),

    path('auth/', include('oauth2_provider.urls')),
]
