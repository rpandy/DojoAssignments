from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

	# 1. "teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
	# 2. "players": Player.objects.filter(curr_team__team_name__contains="Penguins")
	# 3. "players": Player.objects.filter(curr_team__league__name__contains="International Collegiate Baseball Conference"),
	#4. "players": Player.objects.filter(curr_team__league__name__contains="American Conference of Amateur Football").filter(last_name__contains="Lopez")
	#5. "players": Player.objects.filter(curr_team__league__sport__contains="football"),
	# 6."teams": Team.objects.filter(curr_players__first_name__contains="Sophia"),
	# 7. "teams": Team.objects.filter(curr_players__first_name__contains="Sophia"),
	# 8."players": Player.objects.filter(last_name__contains="Flores").exclude(curr_team__team_name__contains="Roughriders"),
	# 9."teams": Team.objects.filter(all_players__first_name="Samuel",all_players__last_name="Evans"),
	# 10. "players": Player.objects.filter(all_teams__team_name__contains="Tiger-Cats"),
	# INCORRECT 11. "teams": Team.objects.filter(all_players__team_name__contains="Vikings"),
	



def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
