import requests
import os
import json
import datetime
from datetime import timedelta
import dateutil.parser
from bs4 import BeautifulSoup
from datetime import datetime

lolesports = requests.get("https://sports.intertops.eu/en/Bets/Esports/League-of-Legends-LPL-Spring/4221")
NCAAB = requests.get("https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068")
NBA = requests.get("https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070")
#NCAAF = requests.get("")
NFL = requests.get("https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018")
Hockey = requests.get("https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064")
allesports = requests.get("https://sports.intertops.eu/en/Bets/Esports/40")
allTennis = requests.get("https://sports.intertops.eu/en/Bets/Tennis/26")

resp = requests.get('https://api.gambitprofit.com/gambit-plays?_sort=PlayDate:DESC')
json_resp = json.loads(resp.content)
sourceFile = open('raw.txt', 'w')

lolsrc = lolesports.content
NCAABsrc = NCAAB.content
NBAsrc = NBA.content
#NCAAFsrc = NCAAF.content
NFLsrc = NFL.content
Hockeysrc = Hockey.content
allEsportssrc = allesports.content
allTennisSrc = allTennis.content


soup1 = BeautifulSoup(lolsrc, 'lxml')
soup2 = BeautifulSoup(NCAABsrc, 'lxml')
soup3 = BeautifulSoup(NBAsrc, 'lxml')
#soup4 = BeautifulSoup(NCAAFsrc, 'lxml')
soup5 = BeautifulSoup(NFLsrc, 'lxml')
soup6 = BeautifulSoup(Hockeysrc, 'lxml')
soup7 = BeautifulSoup(allEsportssrc, 'lxml')

sourceFile = open('raw.txt', 'w')

# Fetch all the games available on Gambit
gambitGames = []
for play in json_resp:
	if play['PlayDate'] > datetime.now().isoformat()[:-3]+'Z':
		d = dateutil.parser.parse(play['PlayDate'])
		gambitGames.append(play['Team1']['Name'])
		gambitGames.append(play['Team2']['Name'])
		
		print(play['Team1']['Name'],play['Team1']['Reward'],play['Team2']['Name'],play['Team2']['Reward'])
		# if int(gambitGames['Team1']['Reward'])<1.3 or int(gambitGames['Team2']['Reward'])<1.3:
		# 	print('This game has 1.3 or below')
		# 	print()
# League of Legends
# -----------------------------------------------------------------------------------------
# links = soup1.find_all('a', class_="seeall cl-e")
# for link in links:
# 	fullLink = link.b.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
# 	print(fullLink, file = sourceFile)

# print("-----------------------------------------------------------------------------------------", file = sourceFile)
# College Basketball
# -----------------------------------------------------------------------------------------
links = soup2.find_all('a', class_="seeall cl-e")
for link in links:
	# Search to see if the game is on Gambit before adding it to the txt
	if link.b.div.string in gambitGames:
		fullLink = link.b.div.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
		print(fullLink, file = sourceFile)

# print("------------------------------------------------------------------------------------------", file = sourceFile)
# NBA
# -----------------------------------------------------------------------------------------
links = soup3.find_all('a', class_="seeall cl-e")
for link in links:
	# Search to see if the game is on Gambit before adding it to the txt
	if link.b.div.string in gambitGames:
		fullLink = link.b.div.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
		print(fullLink, file = sourceFile)

	#This function below prints the contents of the second child div
	#print(link.b.find("div", {"class": "usbot"}).string, file = sourceFile)

# print("-------------------------------------------------------------------------------------------", file = sourceFile)
# College Football
# -----------------------------------------------------------------------------------------
#links = soup4.find_all('a', class_="seeall cl-e")
#for link in links:
#	fullLink = link.b.div.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
#	print(fullLink, file = sourceFile)

# print("--------------------------------------------------------------------------------------------", file = sourceFile)
# NFL
# -----------------------------------------------------------------------------------------
links = soup5.find_all('a', class_="seeall cl-e")
for link in links:
	if link.find('div'):
			# Search to see if the game is on Gambit before adding it to the txt
			if link.b.div.string in gambitGames:
				fullLink = link.b.div.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
				print(fullLink, file = sourceFile)


# print("---------------------------------------------------------------------------------------------", file = sourceFile)
# NHL
# -----------------------------------------------------------------------------------------
links = soup6.find_all('a', class_="seeall cl-e")
for link in links:
	#join function used to remove whitespace and newlines
	#fullLink = ' '.join(link.text.split()) + "; " + "https://sports.intertops.eu" + link.attrs['href']
	# Search to see if the game is on Gambit before adding it to the txt
	if link.b.div.string in gambitGames:
		fullLink = link.b.div.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
		print(fullLink, file = sourceFile)

# print("-----------------------------------------------------------------------------------------------", file = sourceFile)
# All esports
# -----------------------------------------------------------------------------------------
links = soup7.find_all('a', class_="cl-e cl-ttl")
for link in links:		
	string1 = ' '.join(link.text.split())
	index = string1.find(' v ')
	teamOne = string1[:index]
	# Search to see if the game is on Gambit before adding it to the txt
	if teamOne in gambitGames:
		fullLink = teamOne + "; " + "https://sports.intertops.eu" + link.attrs['href']
		print(fullLink, file = sourceFile)


print("--------------------------------------------------- Tennis ----------------------------------------------", file = sourceFile)
# All Tennis
# -----------------------------------------------------------------------------------------
links = soup8.find_all('a', class_="cl-e cl-ttl")
for link in links:
	string1 = ' '.join(link.text.split())
	index = string1.find(' v ')
	teamOne = string1[:index]
	# Search to see if the game is on Gambit before adding it to the txt
	if teamOne in gambitGames:
		fullLink = teamOne + "; " + "https://sports.intertops.eu" + link.attrs['href']
		print(fullLink, file = sourceFile)


sourceFile.close()

# Remove the dupes
lines_seen = set() # holds lines already seen
outfile = open('List_of_Games.txt', "w")
for line in open('raw.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

os.remove("raw.txt")

