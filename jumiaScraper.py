from bs4 import BeautifulSoup
import requests
import time
import sys
import json

class animations:
    def itemAnim(self,subSec):
        animation = [(f"Finding {subSec}."),(f"Finding {subSec}.."),(f"Finding {subSec}..."),(f"Finding {subSec}...."),(f"Finding {subSec}.....")]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

callAnim = animations()


class Fetcher:
    def __init__(self,subSec,pageAmt):
        totpage = 0
        while totpage <pageAmt:
            totpage = totpage + 1
            url = (f"https://www.jumia.co.ke/catalog/?q={subSec}&sort=lowest-price&shipped_from=country_local&page={totpage}")
            site = requests.get(url)

            soup = BeautifulSoup(site.text,'html.parser')
            products = soup.find_all(class_='core')
            gathered = []
            for product in products:
                itemName = product.find(class_='name')
                itemPrice = product.find(class_='prc')

                fillName = itemName.get_text()
                fillPrice = itemPrice.get_text()
                fillLink = (f"https://www.jumia.co.ke{product['href']}")

                gatheredItems = {
                    "name": fillName,
                    "Price": fillPrice,
                    "Link" : fillLink
                }
                
                gathered.append(gatheredItems)

        with open(f"{subSec}.json",'w')as storeData:
            json.dump(gathered,storeData)

        
Iterate = 0

while Iterate != 1:
    print("|||| Welcome to the Jumia Kenya scraper ||||")
    subSec = input("Search for a product (Type 'quit' to exit the program)...... ")

    if subSec == "quit":
        Iterate = 1


    if subSec != "quit":
        pageAmt = int(input("Fetch how many pages? "))
        callAnim.itemAnim(subSec)
        Fetcher(subSec,pageAmt)

else:
    print("Quitting...")

