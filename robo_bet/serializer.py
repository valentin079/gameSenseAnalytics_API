from rest_framework import serializers
from robo_bet.models import Jogo, JogoFinal

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

class JogoFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogoFinal
        fields = '__all__'