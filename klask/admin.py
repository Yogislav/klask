from django.contrib.admin import ModelAdmin, register

from .models import Player, Match, PlayerHistory


@register(Player)
class PlayerAdmin(ModelAdmin):
    ordering = ['id']
    search_fields = ['last_name', 'first_name']
    list_display = [
        'id',
        'last_name',
        'first_name',
        'rating'
    ]
    readonly_fields = [
        'id',
        'rating',
    ]
    
    
@register(Match)
class MatchAdmin(ModelAdmin):
    ordering = ['-date']
    search_fields = ['winner', 'looser', 'date']
    list_display = [
        'id',
        'date',
        'winner',
        'looser'
    ]
    readonly_fields = [
        'id',
        'date',
        'winner',
        'looser'
    ]
    
    
@register(PlayerHistory)
class PlayerHistoryAdmin(ModelAdmin):
    ordering = ['id']
    search_fields = ['player']
    list_display = [
        'id',
        'player',
        'rating',
        'match',
    ]
    readonly_fields = [
        'id',
        'player',
        'rating',
        'match',
    ]