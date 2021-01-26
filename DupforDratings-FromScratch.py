
# coding: utf-8

# In[1]:

import requests
import pandas
from pandas import DataFrame
import csv

from selenium import webdriver
import time
from datetime import datetime
from bs4 import BeautifulSoup

import os
import glob
import pandas as pd


# In[87]:

def get_all_tabs_of_player_page(URL):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source,'html')
    driver.quit()
    tables = soup.find_all('table',{"class":["tablesaw"]})
    tabs_dic = {}
    
    for table in tables:
        tab_name = table['id']
        
        tab_data = [[cell.text for cell in row.find_all(["th","td"])] for row in table.find_all("tr")]
        df = pd.DataFrame(tab_data)
        df.columns = df.iloc[0,:]
        df.drop(index=0,inplace=True)
        
        tabs_dic[tab_name] = df
    return tabs_dic


# In[88]:

nfl = get_all_tabs_of_player_page('https://www.dratings.com/predictor/nfl-football-predictions/')
page1 = nfl.get(list(nfl.keys())[0])
page2 = nfl.get(list(nfl.keys())[1])
page3 = nfl.get(list(nfl.keys())[2])
nfl = page1.append([page2, page3],sort=False)
nfl = nfl[['Teams','Time','Win']]
nfl = nfl.dropna()

nfl['Time'] = nfl['Time'].replace(' Postponed','12/30/209912:59 AM')

nfl['Time'] = pd.to_datetime(nfl['Time'], format='%m/%d/%Y%I:%M %p') 
nfl['Sport']='NFL'


# In[89]:

nba = get_all_tabs_of_player_page('https://www.dratings.com/predictor/nba-basketball-predictions/')
page1 = nba.get(list(nba.keys())[0])
page2 = nba.get(list(nba.keys())[1])
page3 = nba.get(list(nba.keys())[2])
nba = page1.append([page2, page3],sort=False)
nba = nba[['Teams','Time','Win']]
nba = nba.dropna()

nba['Time'] = nba['Time'].replace(' Postponed','12/30/209912:59 AM')

nba['Time'] = pd.to_datetime(nba['Time'], format='%m/%d/%Y%I:%M %p') 
nba['Sport']='NBA'


# In[90]:

ncaab = get_all_tabs_of_player_page('https://www.dratings.com/predictor/ncaa-basketball-predictions/')

page1 = ncaab.get(list(ncaab.keys())[0])
page2 = ncaab.get(list(ncaab.keys())[1])
page3 = ncaab.get(list(ncaab.keys())[2])

ncaab = page1.append([page2, page3],sort=False)

ncaab = ncaab[['Teams','Time','Win']]
ncaab = ncaab.dropna()


ncaab['Time'] = ncaab['Time'].replace(' Postponed','12/30/209912:59 AM')

ncaab['Time'] = pd.to_datetime(ncaab['Time'], format='%m/%d/%Y%I:%M %p') 
ncaab['Sport']='NCAAB'


# In[91]:

ufcmma = get_all_tabs_of_player_page('https://www.dratings.com/predictor/ufc-mma-predictions/')

page1 = ufcmma.get(list(ufcmma.keys())[0])
page2 = ufcmma.get(list(ufcmma.keys())[1])
page3 = ufcmma.get(list(ufcmma.keys())[2])
ufcmma = page1.append([page2, page3],sort=False)
ufcmma = ufcmma[['Fighters','Time','Win']]
ufcmma = ufcmma.rename(columns={"Fighters": "Teams"})

ufcmma = ufcmma.dropna()

ufcmma['Time'] = ufcmma['Time'].replace(' Postponed','12/30/209912:59 AM')

ufcmma['Time'] = pd.to_datetime(ufcmma['Time'], format='%m/%d/%Y%I:%M %p') 
ufcmma['Sport']='UFC MMA'


# In[92]:

#NHL Errors some of the Time Because of a Mishape from the Pages Pulled 

#nhl = get_all_tabs_of_player_page('https://www.dratings.com/predictor/nhl-hockey-predictions/')

#page1 = nhl.get(list(nhl.keys())[0])
#page2 = nhl.get(list(nhl.keys())[1])
#page3 = nhl.get(list(nhl.keys())[2])

#nhl = page1.append([page2, page3],sort=True)
#nhl = nhl[['Teams','Time','Win']]

#nhl = nhl.dropna()

#nhl['Time'] = nhl['Time'].replace(' Postponed','12/30/209912:59 AM')

#nhl['Time'] = pd.to_datetime(nhl['Time'], format='%m/%d/%Y%I:%M %p') 
#nhl['Sport']='NHL'    


# In[94]:

CombinedDF = nba.append([nfl, ncaab, ufcmma],sort=False)
CombinedDF = CombinedDF.rename(columns={"Win": "DRatings Win%"})


start_date = datetime.now()

after_start_date = CombinedDF["Time"] >= start_date
filtered_dates = CombinedDF.loc[after_start_date]

CombinedDFSorted = filtered_dates.sort_values(by='Time')

Teams = CombinedDFSorted["Teams"].str.split(")", n = 1, expand = True) 
CombinedDFSorted["Team 1"]= Teams[0] 
CombinedDFSorted["Team 2"]= Teams[1] 
CombinedDFSorted.drop(columns =["Teams"], inplace = True) 
CombinedDFSorted['Team 1'] = CombinedDFSorted['Team 1'].astype(str) + ')'

Win = CombinedDFSorted["DRatings Win%"].str.split("%", n = 1, expand = True) 
CombinedDFSorted["Team 1 Win %"]= Win[0] 
CombinedDFSorted["Team 2 Win %"]= Win[1] 
CombinedDFSorted.drop(columns =["DRatings Win%"], inplace = True) 
CombinedDFSorted['Team 1 Win %'] = CombinedDFSorted["Team 1 Win %"].astype(str) + '%'

Team1His = CombinedDFSorted["Team 1"].str.split("(", n = 1, expand = True) 
CombinedDFSorted["Team 1 Name"]= Team1His[0] 
CombinedDFSorted["Team 1 History"]= Team1His[1] 
CombinedDFSorted.drop(columns =["Team 1"], inplace = True) 
CombinedDFSorted["Team 1 History"] = '(' + CombinedDFSorted["Team 1 History"].astype(str)

Team2His = CombinedDFSorted["Team 2"].str.split("(", n = 1, expand = True) 
CombinedDFSorted["Team 2 Name"]= Team2His[0] 
CombinedDFSorted["Team 2 History"]= Team2His[1] 
CombinedDFSorted.drop(columns =["Team 2"], inplace = True) 
CombinedDFSorted["Team 2 History"] = '(' + CombinedDFSorted["Team 2 History"].astype(str)

Team1PercSplit = CombinedDFSorted["Team 1 Win %"].str.split("%", n = 1, expand = True) 
CombinedDFSorted["Team 1 as %"]= Team1PercSplit[0] 
CombinedDFSorted["Team 1 %"]= Team1PercSplit[1] 
CombinedDFSorted.drop(columns =["Team 1 Win %"], inplace = True) 
CombinedDFSorted.drop(columns =["Team 1 %"], inplace = True) 

Team2PercSplit = CombinedDFSorted["Team 2 Win %"].str.split("%", n = 1, expand = True) 
CombinedDFSorted["Team 2 as %"]= Team2PercSplit[0] 
CombinedDFSorted["Team 2 %"]= Team2PercSplit[1] 
CombinedDFSorted.drop(columns =["Team 2 Win %"], inplace = True) 
CombinedDFSorted.drop(columns =["Team 2 %"], inplace = True) 

CombinedDFSorted["Team 1 as %"] = CombinedDFSorted["Team 1 as %"].astype(float)
CombinedDFSorted["Team 2 as %"] = CombinedDFSorted["Team 2 as %"].astype(float)

CombinedDFSorted


# In[ ]:




# In[ ]:




# In[ ]:



