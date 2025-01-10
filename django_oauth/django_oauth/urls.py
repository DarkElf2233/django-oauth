from django.contrib import admin
from django.urls import path, include
from myapp.views import ObtainTokenView, RevokeTokenView

urlpatterns = [
    path('adfsdhehtyxqzczq/', admin.site.urls),
    path('api/', include('myapp.urls')),

    path('api/token/', ObtainTokenView.as_view()),
    path('api/token/revoke/', RevokeTokenView.as_view()),

    path('auth/', include('oauth2_provider.urls')),
]
