from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	return render(request, "home.html", {})

#HOME2
def home2(request):
	return render(request, "home2.html", {})


###################################################################################################################################################

#ATLANTA
def hawks(request):
	import requests
	import json

	# ATLANTA General Info 134880
	hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Atlanta%20Hawks")
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
	celticsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Boston%20Celtics")
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
	netsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Brooklyn%20Nets")
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
	hornetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Charlotte%20Hornets")
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
	bullsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Chicago%20Bulls")
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

#CLEVELAND
def cavaliers(request):
	import requests
	import json

	# CAVALIERS General Info 134871
	cavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Cleveland%20Cavaliers")
	cavs_info = json.loads(cavsRE.content)
	# CAVALIERS Last Game 134871
	cavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134871")
	cavs_last = json.loads(cavsLG.content)
	# CAVALIERS Next Game 134871
	cavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134871")
	cavs_next = json.loads(cavsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "cavaliers.html", {'cavs_info': cavs_info, 'cavs_last': cavs_last, 'cavs_next': cavs_next, 'notfound': notfound})

####################################################################################################################################################

#DALLAS
def mavericks(request):
	import requests
	import json

	# MAVERICKS General Info 134875
	mavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Dallas%20Mavericks")
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
	nuggetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Denver_Nuggets")
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

#DETROIT
def pistons(request):
	import requests
	import json

	# PISTONS General Info 134872
	pistonsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Detroit%20Pistons")
	pistons_info = json.loads(pistonsRE.content)
	# PISTONS Last Game 134872
	pistonsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
	pistons_last = json.loads(pistonsLG.content)
	# PISTONS Next Game 134872
	pistonsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")
	pistons_next = json.loads(pistonsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "pistons.html", {'pistons_info': pistons_info, 'pistons_last': pistons_last, 'pistons_next': pistons_next, 'notfound': notfound})

####################################################################################################################################################

#HOUSTON
def rockets(request):
	import requests
	import json

	# ROCKETS Info 134876
	rocketsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Houston%20Rockets")
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

#INDIANA
def pacers(request):
	import requests
	import json

	# PACERS General Info 134873
	pacersRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Indiana%20Pacers")
	pacers_info = json.loads(pacersRE.content)
	# PACERS Last Game Info
	pacersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134873")
	pacers_last = json.loads(pacersLG.content)
	# PACERS Next Game Info
	pacersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134873")
	pacers_next = json.loads(pacersNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "pacers.html", {'pacers_info': pacers_info, 'pacers_last': pacers_last, 'pacers_next': pacers_next, 'notfound': notfound})

####################################################################################################################################################

#UTAH
def jazz(request):
	import requests
	import json

	# JAZZ General Info 134879
	jazzRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Utah_jazz")
	jazz_info = json.loads(jazzRE.content)
	# JAZZ Last Game 134879
	jazzLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134889")
	jazz_last = json.loads(jazzLG.content)
	# JAZZ Next Game 134879
	jazzNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134889")
	jazz_next = json.loads(jazzNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "jazz.html", {'jazz_info': jazz_info, 'jazz_last': jazz_last, 'jazz_next': jazz_next, 'notfound': notfound})

####################################################################################################################################################

#ORLANDO
def magic(request):
	import requests
	import json

	# MAGIC General Info 134883
	magicRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Orlando_Magic")
	magic_info = json.loads(magicRE.content)
	# MAGIC Last Game 134883
	magicLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134883")
	magic_last = json.loads(magicLG.content)
	# MAGIC Next Game 134883
	magicNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134883")
	magic_next = json.loads(magicNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "magic.html", {'magic_info': magic_info, 'magic_last': magic_last, 'magic_next': magic_next, 'notfound': notfound})

####################################################################################################################################################

#SACRAMENTO
def kings(request):
	import requests
	import json

	# KINGS General Info 134869
	kingsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Sacramento_Kings")
	kings_info = json.loads(kingsRE.content)
	# KINGS Last Game 134869
	kingsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134869")
	kings_last = json.loads(kingsLG.content)
	# KINGS Next Game 134869
	kingsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134869")
	kings_next = json.loads(kingsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "kings.html", {'kings_info': kings_info, 'kings_last': kings_last, 'kings_next': kings_next, 'notfound': notfound})


####################################################################################################################################################


#LOS ANGELES LAKERS
def lakers(request):
	import requests
	import json
	# KCal the LAKERS are playing 134867
	lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Los_Angeles_Lakers")
	lakers_info = json.loads(lakersRE.content)
	# LAKERS last game info
	lakersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
	lakers_last = json.loads(lakersLG.content)
	# LAKERS next game info
	lakersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")
	lakers_next = json.loads(lakersNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "lakers.html", {'lakers_info': lakers_info, 'lakers_last': lakers_last, 'lakers_next': lakers_next,'notfound': notfound})


####################################################################################################################################################

#LOS ANGELES CLIPPERS
def clippers(request):
	import requests
	import json

	# CLIPPERS General Info 134866
	clippersRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Los%20Angeles%20Clippers")
	clippers_info = json.loads(clippersRE.content)
	# CLIPPERS last game info 134866
	clippersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134866")
	clippers_last = json.loads(clippersLG.content)
	# CLIPPERS next game info 134866
	clippersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134866")
	clippers_next = json.loads(clippersNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "clippers.html", {'clippers_info': clippers_info, 'clippers_last': clippers_last, 'clippers_next': clippers_next,'notfound': notfound})

####################################################################################################################################################

#MEMPHIS
def grizzlies(request):
	import requests
	import json

	# GRIZZLIES General Info 134877
	grizzRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Memphis_Grizzlies")
	grizz_info = json.loads(grizzRE.content)
	# Last Game info for GRIZZLIES 134877
	grizzLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134877")
	grizz_last = json.loads(grizzLG.content)
	# Next Game info for GRIZZLIES 134877
	grizzNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134877")
	grizz_next = json.loads(grizzNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "grizzlies.html", {'grizz_info': grizz_info, 'grizz_last': grizz_last, 'grizz_next': grizz_next,'notfound': notfound})

####################################################################################################################################################

#MIAMI
def heat(request):
	import requests
	import json

	# HEAT General Info 134882
	heatRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Miami_Heat")
	heat_info = json.loads(heatRE.content)
	# Last Game Info HEAT 134882
	heatLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134882")
	heat_last = json.loads(heatLG.content)
	# Next Game Info HEAT 134882
	heatNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134882")
	heat_next = json.loads(heatNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "heat.html", {'heat_info': heat_info, 'heat_last': heat_last, 'heat_next': heat_next,'notfound': notfound})


####################################################################################################################################################

#MILWAUKEE
def bucks(request):
	import requests
	import json

	# MILWAUKEE BUCKS General Info 134874
	bucksRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Milwaukee_Bucks")
	bucks_info = json.loads(bucksRE.content)
	# Last Game info for BUCKS 134874
	bucksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
	bucks_last = json.loads(bucksLG.content)
	# Next Game info for BUCKS 134874
	bucksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")
	bucks_next = json.loads(bucksNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "bucks.html", {'bucks_info': bucks_info, 'bucks_last': bucks_last, 'bucks_next': bucks_next, 'notfound': notfound})


####################################################################################################################################################

#MINNESOTA 
def twolves(request):
	import requests
	import json

	# T WOLVES General Info 134886
	twolvesRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Minnesota%20Timberwolves")
	twolves_info = json.loads(twolvesRE.content)
	# T-WOLVES Last Game Info
	twolvesLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134886")
	twolves_last = json.loads(twolvesLG.content)
	# T-WOLVES Next Game Info
	twolvesNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134886")
	twolves_next = json.loads(twolvesNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "twolves.html", {'twolves_info': twolves_info, 'twolves_last': twolves_last, 'twolves_next': twolves_next, 'notfound': notfound})

####################################################################################################################################################

#NEW YORK
def knicks(request):
	import requests
	import json

	# KNICKS General Info 134862
	knicksRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=new_york_knicks")
	knicks_info = json.loads(knicksRE.content)
	# KNICKS Last Game 134862
	knicksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134862")
	knicks_last = json.loads(knicksLG.content)
	# KNICKS Next Game 134862
	knicksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134862")
	knicks_next = json.loads(knicksNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "knicks.html", {'knicks_info': knicks_info, 'knicks_last': knicks_last, 'knicks_next': knicks_next, 'notfound': notfound})

####################################################################################################################################################

#OKLAHOMA
def thunder(request):
	import requests
	import json

	# OKLAHOMA General Info 134887
	thunderRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Oklahoma_City_Thunder")
	thunder_info = json.loads(thunderRE.content)
	# OKLAHOMA Last Game 134887
	thunderLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134887")
	thunder_last = json.loads(thunderLG.content)
	# OKLAHOMA Next Game 134887
	thunderNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134887")
	thunder_next = json.loads(thunderNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "thunder.html", {'thunder_info': thunder_info, 'thunder_last': thunder_last, 'thunder_next': thunder_next, 'notfound': notfound})

####################################################################################################################################################

#PELICANS
def pelicans(request):
	import requests
	import json

	# PELICANS General Info 134878
	pelicansRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=New%20Orleans%20Pelicans")
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

#RAPTORS
def raptors(request):
	import requests
	import json

	# RAPTORS General Info 134864
	raptorsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Toronto_Raptors")
	raptors_info = json.loads(raptorsRE.content)
	# RAPTORS Last Game 134864
	raptorsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134864")
	raptors_last = json.loads(raptorsLG.content)
	# RAPTORS Next Game 134864
	raptorsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134864")
	raptors_next = json.loads(raptorsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "raptors.html", {'raptors_info': raptors_info,'raptors_last': raptors_last, 'raptors_next': raptors_next, 'notfound': notfound})

####################################################################################################################################################

#SIXERS
def sixers(request):
	import requests
	import json

	#SIXERS General Info 134863
	sixersRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=philadelphia_76ers")
	sixers_info = json.loads(sixersRE.content)
	#SIXERS Last Game 134863
	sixersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134863")
	sixers_last = json.loads(sixersLG.content)
	#SIXERS Next Game 134863
	sixersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134863")
	sixers_next = json.loads(sixersNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "sixers.html", {'sixers_info': sixers_info,'sixers_last': sixers_last, 'sixers_next': sixers_next, 'notfound': notfound})

####################################################################################################################################################

#SPURS
def spurs(request):
	import requests
	import json

	# SPURS General Info 134879
	spursRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=San_Antonio_Spurs")
	spurs_info = json.loads(spursRE.content)
	# SPURS Last Game 134879
	spursLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134879")
	spurs_last = json.loads(spursLG.content)
	# SPURS Next Game 134879
	spursNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134879")
	spurs_next = json.loads(spursNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "spurs.html", {'spurs_info': spurs_info,'spurs_last': spurs_last, 'spurs_next': spurs_next, 'notfound': notfound})

####################################################################################################################################################

#SUNS
def suns(request):
	import requests
	import json

	# SUNS General Info 134868
	sunsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Phoenix_Suns")
	suns_info = json.loads(sunsRE.content)
	# SUNS Last Game 134868
	sunsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134868")
	suns_last = json.loads(sunsLG.content)
	# SUNS Next Game 134868
	sunsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134868")
	suns_next = json.loads(sunsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "suns.html", {'suns_info': suns_info,'suns_last': suns_last, 'suns_next': suns_next, 'notfound': notfound})

####################################################################################################################################################

#TRAILBLAZERS
def trailblazers(request):
	import requests
	import json

	# PORTLAND General Info 134888
	portlandRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Portland_Trail_Blazers")
	portland_info = json.loads(portlandRE.content)
	# PORTLAND Last Game 134888
	portlandLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")
	portland_last = json.loads(portlandLG.content)
	# PORTLAND Next Game 134888
	portlandNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134888")
	portland_next = json.loads(portlandNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "blazers.html", {'portland_info': portland_info,'portland_last': portland_last, 'portland_next': portland_next, 'notfound': notfound})

####################################################################################################################################################

#WARRIORS
def warriors(request):
	import requests
	import json

	# WARRIORS General Info 134865
	warriorsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Golden%20State%20Warriors")
	warriors_info = json.loads(warriorsRE.content)
	# WARRIORS Last Game 134865
	warriorsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134865")
	warriors_last = json.loads(warriorsLG.content)
	# WARRIORS Next Game 134865
	warriorsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134865")
	warriors_next = json.loads(warriorsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "warriors.html", {'warriors_info': warriors_info,'warriors_last': warriors_last, 'warriors_next': warriors_next, 'notfound': notfound})

####################################################################################################################################################

#WASHINGTON
def wizards(request):
	import requests
	import json

	# WIZARDS General Info 134884
	wizardsRE = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Washington_Wizards")
	wizards_info = json.loads(wizardsRE.content)
	# WIZARDS Last Game 134884
	wizardsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134884")
	wizards_last = json.loads(wizardsLG.content)
	# WIZARDS Next Game 134884
	wizardsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134884")
	wizards_next = json.loads(wizardsNG.content)

	notfound = "If no game shows, it's because this team didn't qualify for the remainder of the 2020 season or the next game is to be determined"

	return render(request, "wizards.html", {'wizards_info': wizards_info,'wizards_last': wizards_last, 'wizards_next': wizards_next, 'notfound': notfound})


####################################################################################################################################################



