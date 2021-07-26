from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.filter(name__contains='women'),
		"teams": Team.objects.filter(team_name__startswith='T').order_by('team_name').reverse(),
		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua').union( 
                        Player.objects.filter(first_name='Alexander').union(
                                Player.objects.filter(first_name='Wyatt'))),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
