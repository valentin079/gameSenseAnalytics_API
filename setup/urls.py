from django.contrib import admin
from django.urls import path, include
from robo_bet.views import JogosViewSet, JogosFinaisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos',JogosViewSet, basename='Jogos')
router.register('jogosFinais',JogosFinaisViewSet, basename='JogosFinais')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
