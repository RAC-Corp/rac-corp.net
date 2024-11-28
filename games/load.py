import requests

games = {
  'iiaf': 'https://games.roblox.com/v1/games?universeIds=4791664217',
  'iiaf': 'https://games.roblox.com/v1/games?universeIds=4128847839',
  'rogessr': 'https://games.roblox.com/v1/games?universeIds=6743414374'
}

for game in games:
	try:
		r = requests.get(games[game]).text
	except Exception as e:
		print(str(e))
	else:
		print(r)