from bs4 import BeautifulSoup
import requests
import time
import sys


subSec = input("Enter desired category you want to get jumia deals......")
sort = int(input("Choose sort method.... (1)Popularity {*default*} , (2)Newest arrivals , (3)Low to high , (4)High to low , (5) Product rating..."))

if sort == 1:
    sortType = ""
elif sort == 2:
    sortType = "&sort=newest"
elif sort == 3:
    sortType ="&sort=lowest-price"
elif sort == 4:
    sortType = "&sort=highest-price"
elif sort == 5:
    sortType ="&sort=rating"
else:
    print("No such method...")
    print("Using default")
    sortType = ""

#animation sequence
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

url = (f"https://www.jumia.co.ke/catalog/?q={subSec}{sortType}")
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

print("Jumia scraper by Brian.......more features soon..")
print("Goodbye!")
