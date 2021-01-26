from tika import parser
import requests
from PyPDF2 import PdfFileReader
import io
import PyPDF2
import urllib.request
import pikepdf
import lxml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import re
import time 
import csv
import traceback
import re





file1 = open('bookiedata.txt', 'w') 
L = [] 
s = "Bookie data\n"
  
# Writing a string to file 
file1.write(s) 
  
# Writing multiple strings 
# at a time 

  








options = Options()
# options.headless = True

driver = webdriver.Chrome('chromedriver', options=options)

parcel_url = 'https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
driver.get(parcel_url)

xpathElement = driver.find_element_by_xpath('//*[@id="1000"]/div/fieldset/div')


ids = driver.find_elements_by_xpath('//*[@id="1000"]/div/fieldset/div')


#print(ids)
html_data = driver.page_source
soup = BeautifulSoup(html_data, "lxml")
games = soup.findAll("div", {"class": "tbody"})
newGames = soup.find_all('a', href=True)
for a in newGames:
    links="https://sports.intertops.eu"+str( a['href'])+'\n'
    file1.writelines(re.sub(' +', ' ', links))
    #print(a.text)
#print(newGames)

# for each in games:
#     a=each.find_all('div')
#     #print(a)
#     for table in a:
#         file1.writelines(re.sub(' +', ' ', table.text))
        
#         #print()
#         break

#     # print(a)
#     # print(len(a))

#     break

# Closing file 
file1.close() 
  
# Checking if the data is 
# written to file or not 
file1 = open('bookiedata.txt', 'r') 
print(file1.read()) 
file1.close() 

# for ii in ids:
#     #print ii.tag_name
#     print (ii)

driver.close()

# print(xpathElement.text_content())

# html_data = driver.page_source
# soup = BeautifulSoup(html_data, "lxml")
# sale_data = soup.find('table', id="Sales Detail").find_all('tr')








# resp = requests.get('https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068')

# print(resp.content)

# f = open("demofile2.html", "a")
# f.write(resp.content)
# f.close()

# json_resp = json.loads(resp.content)

# for i in json_resp:
#     print(i)
    


