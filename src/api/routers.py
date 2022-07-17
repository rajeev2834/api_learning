from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('auth/', include('djoser.urls'), name='djoser'),
    path('auth/', include('djoser.urls.jwt'), name='djoser-jwt'),
    path('auth/', include('djoser.urls.authtoken'), name='djoser-authtoken'),
]

urlpatterns = urlpatterns + router.urls