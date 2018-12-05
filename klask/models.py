from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Imię')
    last_name = models.CharField(max_length=64, verbose_name='Nazwisko')
    rating = models.IntegerField(verbose_name='Ranking', default=1000)
    
    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'
    

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data meczu')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_winner', verbose_name='Zwycięzca')
    looser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_looser',  verbose_name='Przegrany')
    
    def __str__(self):
        return "Mecz {0}".format(self.id)

    class Meta:
        verbose_name = 'Mecz'
        verbose_name_plural = 'Mecze'

    
class PlayerHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Zawodnik')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Mecz')
    rating = models.IntegerField(verbose_name='Ranking')
    
    def __str__(self):
        return "Mecz {0}".format(self.id)

    class Meta:
        verbose_name = 'Historia zawodnika'
        verbose_name_plural = 'Historie zawodnika'
