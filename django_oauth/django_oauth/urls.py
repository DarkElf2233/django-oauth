from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(oauth2_urls)),
    path('api/', include('app.urls')),
]
