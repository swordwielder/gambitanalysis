import requests
from bs4 import BeautifulSoup

lolesports = requests.get("https://sports.intertops.eu/en/Bets/Esports/League-of-Legends-LPL-Spring/4221")
lolesports.status_code
lolsrc = lolesports.content
soup = BeautifulSoup(lolsrc, 'lxml')
links = soup.find_all("a")
links = soup.find_all('a', class_="seeall cl-e")
sourceFile = open('demo.txt', 'w')

for link in links:
	fullLink = link.b.string + "; " + "https://sports.intertops.eu" + link.attrs['href']
	print(fullLink, file = sourceFile)
sourceFile.close()
