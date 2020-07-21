from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	import requests
	import json

	# ATLANTA General Info 134880
	hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Atlanta%20Hawks")
	hawks_info = json.loads(hawksRE.content)
	# ATLANTA Last Game 134880
	hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
	# ATLANTA Next Game 134880
	hawksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")

	return render(request, "home.html", {'hawks': hawks_info})
