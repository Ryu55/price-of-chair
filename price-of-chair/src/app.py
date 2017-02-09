#import request library to make http requests
#import the Beautifulsoup package from bs4
import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")

#this will be our html content to search through
content = request.content

#use Beautifulsoup to search through the content variable using the html parser
soup = BeautifulSoup(content, "html.parser")


#find the elment we're looking for from the html page
# <span itemprop="price" class="now-price"> £229.00 </span>
#we're looking for span tags with "itemprop"="price" and class="now-price"
element = soup.find("span", {"itemprop": "price", "class": "now-price"})

#store the data in a variable called string_price
#use .strip() to remove all leading and trailing whitespace on element.text
string_price = element.text.strip()

#the value returned is a string, but let's convert it to a number so python
#can use it
#use slice [:] to get the numbers after the £ symbol
price_without_symbol = string_price[1:]
price = float(price_without_symbol)

#if the price is greater than 200, don't buy the chair
#if the price is less than 200, buy the chair
print("The current price is {}".format(string_price))
if price < 200:
    print("You should buy the chair!")
else:
    print("Do not buy, it's too expensive!")
