from rest_framework import viewsets
from robo_bet.models import Jogo
from robo_bet.serializer import JogoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class JogosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os jogos"""
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]