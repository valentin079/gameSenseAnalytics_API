from django.contrib import admin
from robo_bet.models import Jogo

class Jogos(admin.ModelAdmin):
    list_display = ('id','time','home','goalHome','away','goalAway','apHome','apAway','shotsHome','shotsAway','cornerHome','cornerAway')
    search_fields = ('home','away','time')
    list_per_page = 20

admin.site.register(Jogo, Jogos)
