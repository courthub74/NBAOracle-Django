from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	return render(request, "home.html", {})


###################################################################################################################################################

#ATLANTA
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

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "hawks.html", {'hawks_info': hawks_info, 'hawks_last': hawks_last, 'hawks_next': hawks_next, 'notfound': notfound})



####################################################################################################################################################


#BOSTON
def celtics(request):
	import requests
	import json

	# CELTICS General Info 134860
	celticsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Boston%20Celtics")
	celtics_info = json.loads(celticsRE.content)
	# CELTICS Last Game 134860
	celticsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134860")
	celtics_last = json.loads(celticsLG.content)
	# CELTICS Next Game 134860
	celticsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134860")
	celtics_next = json.loads(celticsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "celtics.html", {'celtics_info': celtics_info, 'celtics_last': celtics_last, 'celtics_next': celtics_next, 'notfound': notfound})


####################################################################################################################################################

#BROOKLYN
def nets(request):
	import requests
	import json

	# NETS General Info 134861
	netsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Brooklyn%20Nets")
	nets_info = json.loads(netsRE.content)
	# NETS Last Game 134861
	netsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134861")
	nets_last = json.loads(netsLG.content)
	# NETS Next Game 134861
	netsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134861")
	nets_next = json.loads(netsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "nets.html", {'nets_info': nets_info, 'nets_last': nets_last, 'nets_next': nets_next, 'notfound': notfound})

####################################################################################################################################################

#CHARLOTTE
def hornets(request):
	import requests
	import json

	# HORNETS General Info 134881
	hornetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Charlotte%20Hornets")
	hornets_info = json.loads(hornetsRE.content)
	# HORNETS Last Game Info 134881
	hornetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134881")
	hornets_last = json.loads(hornetsLG.content)
	# HORNETS Next Game Info 134881
	hornetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134881")
	hornets_next = json.loads(hornetsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "hornets.html", {'hornets_info': hornets_info, 'hornets_last': hornets_last, 'hornets_next': hornets_next, 'notfound': notfound})

####################################################################################################################################################

#CHICAGO
def bulls(request):
	import requests
	import json

	# BULLS General Info 134870
	bullsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Chicago%20Bulls")
	bulls_info = json.loads(bullsRE.content)
	# BULLS Last Game Info 134870
	bullsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134870")
	bulls_last = json.loads(bullsLG.content)
	# BULLS Next Game Info 134870
	bullsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134870")
	bulls_next = json.loads(bullsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "bulls.html", {'bulls_info': bulls_info, 'bulls_last': bulls_last, 'bulls_next': bulls_next, 'notfound': notfound})

####################################################################################################################################################

#DALLAS
def mavericks(request):
	import requests
	import json

	# MAVERICKS General Info 134875
	mavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Dallas%20Mavericks")
	mavs_info = json.loads(mavsRE.content)
	# MAVERICKS Last Game 134875
	mavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134875")
	mavs_last = json.loads(mavsLG.content)
	# MAVERICKS Next Game 134875
	mavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134875")
	mavs_next = json.loads(mavsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "mavs.html", {'mavs_info': mavs_info, 'mavs_last': mavs_last, 'mavs_next': mavs_next, 'notfound': notfound})

####################################################################################################################################################

#DENVER
def nuggets(request):
	import requests
	import json

	# NUGGETS Info Parsed 134885
	nuggetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Denver_Nuggets")
	nuggets_info = json.loads(nuggetsRE.content)
	# NUGGETS Last Game 134885
	nuggetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134885")
	nuggets_last = json.loads(nuggetsLG.content)
	# NUGGETS Next Game 134885
	nuggetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134885")
	nuggets_next = json.loads(nuggetsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "nuggets.html", {'nuggets_info': nuggets_info, 'nuggets_last': nuggets_last, 'nuggets_next': nuggets_next, 'notfound': notfound})


####################################################################################################################################################

#HOUSTON
def rockets(request):
	import requests
	import json

	# ROCKETS Info 134876
	rocketsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Houston%20Rockets")
	rockets_info = json.loads(rocketsRE.content)
	# ROCKETS Last Game Info 134876
	rocketsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134876")
	rockets_last = json.loads(rocketsLG.content)
	# ROCKETS Next Game Info 134876
	rocketsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134876")
	rockets_next = json.loads(rocketsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "rockets.html", {'rockets_info': rockets_info, 'rockets_last': rockets_last, 'rockets_next': rockets_next, 'notfound': notfound})

####################################################################################################################################################


#LAKERS
def lakers(request):
	import requests
	import json
	# KCal the LAKERS are playing 134867
	lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los_Angeles_Lakers")
	lakers_info = json.loads(lakersRE.content)
	# LAKERS last game info
	lakersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
	lakers_last = json.loads(lakersLG.content)
	# LAKERS next game info
	lakersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")
	lakers_next = json.loads(lakersNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "lakers.html", {'lakers': lakers_info, 'lakers_last': lakers_last, 'lakers_next': lakers_next,'notfound': notfound})


####################################################################################################################################################

#MILWAUKEE
def bucks(request):
	import requests
	import json

	# MILWAUKEE BUCKS General Info 134874
	bucksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Milwaukee_Bucks")
	bucks_info = json.loads(bucksRE.content)
	# Last Game info for BUCKS 134874
	bucksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
	bucks_last = json.loads(bucksLG.content)
	# Next Game info for BUCKS 134874
	bucksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")
	bucks_next = json.loads(bucksNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "bucks.html", {'bucks': bucks_info, 'bucks_last': bucks_last, 'bucks_next': bucks_next, 'notfound': notfound})


####################################################################################################################################################


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

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "pelicans.html", {'pelicans_info': pelicans_info,'pelicans_last': pelicans_last, 'pelicans_next': pelicans_next, 'notfound': notfound})

####################################################################################################################################################

#TRAILBLAZERS
def trailblazers(request):
	import requests
	import json

	# PORTLAND General Info 134888
	portlandRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Portland_Trail_Blazers")
	portland_info = json.loads(portlandRE.content)
	# PORTLAND Last Game 134888
	portlandLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")
	portland_last = json.loads(portlandLG.content)
	# PORTLAND Next Game 134888
	portlandNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134888")
	portland_next = json.loads(portlandNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "blazers.html", {'portland_info': portland_info,'portland_last': portland_last, 'portland_next': portland_next, 'notfound': notfound})




