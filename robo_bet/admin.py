from django.contrib import admin
from robo_bet.models import Jogo, JogoFinal

class Jogos(admin.ModelAdmin):
    list_display = ('id','time','home','goalHome','away','goalAway','apHome','apAway','shotsHome','shotsAway','cornerHome','cornerAway', 'date_game')
    search_fields = ('home','away','time')
    list_per_page = 20

class JogosFinais(admin.ModelAdmin):
    list_display = ('id','home','goalHomeFinal','away','goalAwayFinal','apHomeFinal','apAwayFinal','shotsHomeFinal','shotsAwayFinal','cornerHomeFinal','cornerAwayFinal')
    search_fields = ('home','away')
    list_per_page = 20

admin.site.register(Jogo, Jogos)
admin.site.register(JogoFinal, JogosFinais)