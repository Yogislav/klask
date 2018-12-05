from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

from elo import rate_1vs1
from decimal import Decimal

from . import models
from .forms import NewPlayerForm, NewMatchForm


def index(request):
    return render(request, 'index.html', {'players': models.Player.objects.order_by('-rating', 'last_name') })

def new_player(request):
    form = NewPlayerForm()
    if request.method == 'POST':
        form = NewPlayerForm(request.POST)
        if form.is_valid():
            player = models.Player.objects.create(first_name=form.cleaned_data.get('first_name'), 
                                                  last_name=form.cleaned_data.get('last_name'))
            player.save()
            player_history = models.PlayerHistory.objects.create(player=player, rating=player.rating)
            player_history.save()
            
            messages.success(request, "Dodano nowego zawodnika")
            return redirect(reverse('home'))
        else:
            return render(request, 'new_player.html', { 'form': form })
            
    return render(request, 'new_player.html', { 'form': form })

def new_match(request):
    form = NewMatchForm()
    if request.method == 'POST':
        form = NewMatchForm(request.POST)
        if form.is_valid():
            winner = form.cleaned_data.get('winner')
            looser = form.cleaned_data.get('looser')
            elo = rate_1vs1(int(winner.rating), int(looser.rating))
            
            match = models.Match.objects.create(winner=winner, looser=looser)
            match.save()
            
            winner.rating = int(round(Decimal(elo[0]), 0))
            winner.save()
            looser.rating = int(round(Decimal(elo[1]), 0))
            looser.save()
            
            winner_history = models.PlayerHistory.objects.create(player=winner, match=match, rating=winner.rating)
            winner_history.save()
            looser_history = models.PlayerHistory.objects.create(player=looser, match=match, rating=looser.rating)
            looser_history.save()
            
            messages.success(request, "Zarejestrowany mecz.\n Nowe ELO dla {0} {1}: {2}\nNowe ELO dla {3} {4}: {5}\n"
                .format(winner.first_name, winner.last_name, winner.rating, looser.first_name, looser.last_name, looser.rating))
            return redirect(reverse('home'))
        else:
            return render(request, 'new_match.html', { 'form': form })
            
    return render(request, 'new_match.html', { 'form': form })
    
def player_history(request):
    return HttpResponse("PLAYER HISTORY")