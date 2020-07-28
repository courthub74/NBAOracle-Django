from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	return render(request, "home.html", {})

	####################################################################################################################################################

#HAWKS
def hawks(request):
	import requests
	import json

	# ATLANTA General Info 134880
	hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Atlanta%20Hawks")
	hawks_info = json.loads(hawksRE.content)

	# ATLANTA Last Game 134880
	hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
	hawks_last = json.loads(hawksLG.content)

	# ATLANTA Next Game 134880
	hawksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")
	hawks_next = json.loads(hawksNG.content)


	return render(request, "hawks.html", {'hawks_info': hawks_info, 'hawks_last': hawks_last, 'hawks_next': hawks_next})


	####################################################################################################################################################

#LAKERS
def lakers(request):
	import requests
	import json
	# KCal the LAKERS are playing 134867
	lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los_Angeles_Lakers")

	lakers_info = json.loads(lakersRE.content)

	testers = lakersRE

	return render(request, "lakers.html", {'lakers': lakers_info})


#PELICANS
def pelicans(request):
	import requests
	import json

	# PELICANS General Info 134878
	pelicansRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=New%20Orleans%20Pelicans")
	pelicans_info = json.loads(pelicansRE.content)
	# PELICANS Last Game 134878
	pelicansLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134878")
	pelicans_last = json.loads(pelicansLG.content)
	# PELICANS Next Game 134878
	pelicansNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134878")
	pelicans_next = json.loads(pelicansNG.content)


	# homeTeamNOP = ["results"][0]["strHomeTeam"]
	# awayTeamNOP = ["results"][0]["strAwayTeam"]
	# homeScoreNOP = ["results"][0]["intHomeScore"]
	# awayScoreNOP = ["results"][0]["intAwayScore"]

	# def win():
	# 	if int(homeScoreNOP) < 80 and int(awayScoreNOP) < 80:
	# 		return "Game In Progress"
	# 	elif homeTeamNOP == "New Orleans Pelicans" and homeScoreNOP > awayScoreNOP:
	# 		return "Pelicans Win"
	# 	elif awayTeamNOP == "New Orleans Pelicans" and awayScoreNOP > homeScoreNOP:
	# 		return "Pelicans Win"
	# 	else:
	# 		return "Pelicans Lose"

	# win()

	# win = win()
	return render(request, "pelicans.html", {'pelicans_info': pelicans_info,'pelicans_last': pelicans_last, 'pelicans_next': pelicans_next})


