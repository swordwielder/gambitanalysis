from tika import parser
# from helpers.filewriters import write_to_csv, write_to_json
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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import json
import re
import time 
import csv
import traceback





options = Options()
# options.headless = True

driver = webdriver.Chrome('chromedriver', options=options)
full_data = []
url = 'https://gambitprofit.com/'
tokens = 10000



def get_game_data(gambit_html):
    try:
        soup = BeautifulSoup(gambit_html, "lxml")
        mydivs = soup.findAll("div", {"id": "appenddata"})
        print(mydivs)
        # for i in mydivs:
        #     print(i)
    except Exception as err:
        print('damnit unixfy')
        print(err)
        

    
def search_gambit(url,tokens):
    # time.sleep(3)
    driver.get(url)
    # driver.manage().timeouts().implicitlywait(30 timeunit.seconds). 
    # time.sleep(3)
    # tokenInput = driver.find_element_by_xpath('//*[@id="tokenAmount"]')
    # tokenInput.send_code(tokens)

    # tokenSubmit = driver.find_element_by_xpath('//*[@id="tokenSubmitBtn"]')
    # tokenSubmit.click()

    gambit_html_data = driver.page_source
    get_game_data(gambit_html_data)


driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
delay = 4
if 'Home | Gambit Profit' in driver.title:
    print('Executing....')
    try:
        # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH  , '//*[@id="appendData"]')))
        gambit_html = driver.page_source
        # print(type(gambit_html))
        soup = BeautifulSoup(gambit_html, features="lxml")
        mydivs = soup.find_all("div", class_="list row")
        # land_data = soup.findAll("div", {"class": "list row"})
        
        print(mydivs)
        # print(gambit_html)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
else:
    print('guess not')

driver.close()


# f = open("sample.html", "a")
# f.write(gambit_html)
# f.close()

# try:
#     search_gambit(url,tokens)
# except Exception as err:
#     print('Damnit unixfy, your website is messed up')
#     print(err.with_traceback)