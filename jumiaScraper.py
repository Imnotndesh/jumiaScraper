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

    def innAnim(self):
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

z = animations()


class Fetcher:
    def jumiaFetcher(self,subSec,pageAmt):
        z.innAnim()
        totpage = 0
        while totpage <pageAmt:
            totpage = totpage + 1
            url = (f"https://www.jumia.co.ke/catalog/?q={subSec}&sort=lowest-price&shipped_from=country_local&page={totpage}")
            site = requests.get(url)

            soup = BeautifulSoup(site.text,'html.parser')
            products = soup.find_all(class_='core')
            for product in products:
                itemName = product.find(class_='name')
                itemPrice = product.find(class_='prc')

                finalName = (f"Product : {itemName.get_text()}")
                finalPrice = (f" Discounted price : {itemPrice.get_text()}")
                finalLink = (f"Url : https://www.jumia.co.ke{product['href']}")
                print(finalName)
                print(finalPrice)
                print(finalLink)
                print("*************************************")
                print(" ")


            
x=Fetcher()
program = 0

while program != 1:
    print("|||| Welcome to the Jumia Kenya scraper ||||")
    subSec = input("Search for a product (Type 'quit' to exit the program)...... ")

    if subSec == "quit":
        program = 1


    if subSec != "quit":
        pageAmt = int(input("Fetch how many pages? "))
        z.itemAnim(subSec)
        x.jumiaFetcher(subSec,pageAmt)

else:
    print("Quitting...")

