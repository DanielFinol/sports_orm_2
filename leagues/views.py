from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
        
	context = {
		"leagues": League.objects.filter(name__contains='women'),
		"teams": Team.objects.filter(team_name__startswith='T').order_by('team_name').reverse(),
		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua').union( 
                           Player.objects.filter(first_name='Alexander').union(
                           Player.objects.filter(first_name='Wyatt'))),
                "teams_1": Team.objects.filter(league__name='Atlantic Soccer Conference'),
                "players_2": Player.objects.filter(curr_team__team_name="Penguins"),
                "players_3": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
                "players_5": Player.objects.filter(curr_team__league__sport='Soccer'),
                "leagues_7": League.objects.filter(teams__curr_players__first_name='Sophia'),
                "teams_12": Player.objects.get(first_name='Jacob', last_name='Gray').all_teams.exclude(
                        location='Oregon', team_name='Colts'),
                "teams_14": Team.objects.annotate(tam=Count('all_players')).filter(tam__gte=12),
                "players_15": Player.objects.annotate(n_equipos=Count('all_teams')).order_by('n_equipos'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
