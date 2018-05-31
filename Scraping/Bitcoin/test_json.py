from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import requests
from urllib.request import urlopen

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

chrome_dirver = os.getcwd() + "/chromedriver"

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_dirver)
siteName = "http://american-driver.herokuapp.com/magazines.json"
#driver.get(siteName)

site = urlopen(siteName)
data = json.load(site)

for element in data: 
    for iterate in element:
        print("Key: {},  Value: {}".format(iterate, element[iterate]))

