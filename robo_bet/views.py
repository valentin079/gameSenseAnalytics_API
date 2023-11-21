from rest_framework import viewsets
from robo_bet.models import Jogo, JogoFinal
from robo_bet.serializer import JogoSerializer, JogoFinalSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class JogosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os jogos"""
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class JogosFinaisViewSet(viewsets.ModelViewSet):
    """Exibindo estatísticas finais dos jogos"""
    queryset = JogoFinal.objects.all()
    serializer_class = JogoFinalSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]