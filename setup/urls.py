from django.contrib import admin
from django.urls import path, include
from robo_bet.views import JogosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos',JogosViewSet, basename='Jogos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
