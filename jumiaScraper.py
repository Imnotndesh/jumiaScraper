from bs4 import BeautifulSoup
import requests
import time
import sys

def anim():
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")

class Fetcher:
    print("***Jumia Section***")
    def jumiaFetcher(self,subSec):
        anim()
        totpage = 0
        while totpage <5:
            totpage = totpage + 1
            url = (f"https://www.jumia.co.ke/catalog/?q={subSec}&sort=lowest-price&shipped_from=country_local&page={totpage}")
            site = requests.get(url)

            soup = BeautifulSoup(site.text,'html.parser')
            products = soup.find_all(class_='core')
            for product in products:
                imageLink = product.find(class_="img")
                itemName = product.find(class_='name')
                itemPrice = product.find(class_='prc')

                print(f"Product : {itemName.get_text()}")
                print(f" Discounted price : {itemPrice.get_text()}")
                print (f"Url : https://www.jumia.co.ke{product['href']}")
                print("*************************************")
                print(" ")
            


subSec = input("Search for product...... ")

x=Fetcher()
x.jumiaFetcher(subSec)
