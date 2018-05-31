from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import urllib.request
import os, json, csv

coinsApi = "https://coincheckup.com/data/prod/201805292233/coins.json"
sitName = "https://coincheckup.com/"

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()
try:
    coins_api_response = opener.open(coinsApi)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domanin")
else:
    coin_info = {}
    market_overview = []
    data = json.load(coins_api_response)
        
    for element in data[:10]:
        coin_resource_api = "https://coincheckup.com/data/prod/201805292233/assets/" + element["id"] + ".json"
        coin_rs_api_response = opener.open(coin_resource_api)
        coin_resource = json.load(coin_rs_api_response)
        
        coin_info = {
        "id": element["id"],
        "name":    element["name"],
        "symbol": element["symbol"],
        "img" : "https://coincheckup.com" + "/images/coins/" + element["id"] + "-" + coin_resource["logos"]["logo"] + ".png",
        "website_url" : coin_resource["research"]["website_url"],
        "whitepaper_url" : coin_resource["research"]["whitepaper_url"],
        }
        market_overview.append(coin_info)


    """Write into CSV file"""
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['Coin ID', 'Coin Name', 'Coin Symbol', 'Coin Image', 'Coin Website', 'Coin Whitepaper']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for element in market_overview:
            writer.writerow({'Coin ID': element["id"], 'Coin Name': element["name"],
            'Coin Symbol' : element["symbol"], 'Coin Image' : element["img"], 
            'Coin Website' : element["website_url"], 'Coin Whitepaper' : element["whitepaper_url"] })

    opener.close()