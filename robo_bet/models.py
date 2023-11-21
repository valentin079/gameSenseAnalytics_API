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

    def __str__(self):
        return f"{self.home} vs {self.away}"
