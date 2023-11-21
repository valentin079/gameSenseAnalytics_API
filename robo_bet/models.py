from django.db import models

class Jogo(models.Model):
    time = models.BigIntegerField(default=0)
    home = models.CharField(max_length=60)
    goalHome = models.BigIntegerField(default=0)
    away = models.CharField(max_length=60)
    goalAway = models.BigIntegerField(default=0)
    apHome = models.BigIntegerField(default=0)
    apAway = models.BigIntegerField(default=0)
    shotsHome = models.BigIntegerField(default=0)
    shotsAway = models.BigIntegerField(default=0)
    cornerHome = models.BigIntegerField(default=0)
    cornerAway = models.BigIntegerField(default=0)
    date_game = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.home} vs {self.away}"
    
class JogoFinal(models.Model):
    home = models.CharField(max_length=60)
    goalHomeFinal = models.BigIntegerField(default=0)
    away = models.CharField(max_length=60)
    goalAwayFinal = models.BigIntegerField(default=0)
    apHomeFinal = models.BigIntegerField(default=0)
    apAwayFinal = models.BigIntegerField(default=0)
    shotsHomeFinal = models.BigIntegerField(default=0)
    shotsAwayFinal = models.BigIntegerField(default=0)
    cornerHomeFinal = models.BigIntegerField(default=0)
    cornerAwayFinal = models.BigIntegerField(default=0)
  
    def __str__(self):
        return f"{self.home} vs {self.away}"
