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
        url = (f"https://www.jumia.co.ke/catalog/?q={subSec}&sort=lowest-price&shipped_from=country_local")
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
    
    def jamboFetcher(self,subSec):
        print("***Jamboshop section***")
        anim()
        url = (f"https://www.jamboshop.com/search?k={subSec}")

        site = requests.get(url)
        soup = BeautifulSoup(site.text,'html.parser')

        for products in soup.find_all(class_="productDetailsBox"):

            itemName = products.find(class_='prd-title').text.strip()
            itemPrice = products.find(class_='offer-price').text.strip()
            itemLink = products.find(class_='title')
            link = (f"https://www.jamboshop.com/{itemLink['href']}")
            
            print(f"Name: {itemName}")
            print(f"Price: {itemPrice}")
            print(f"link: {link}")
            print("***********************")

        print("Jumia scraper by Brian.......more features soon..")
        print("Goodbye!")



subSec = input("Search for product...... ")

x=Fetcher()
x.jumiaFetcher(subSec)
x.jamboFetcher(subSec)
