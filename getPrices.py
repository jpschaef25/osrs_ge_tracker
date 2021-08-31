import requests
from bs4 import BeautifulSoup
from datetime import datetime
from Item import Item

url = 'https://prices.runescape.wiki/api/v1/osrs/latest'

headers = {
    'User-Agent': 'TestHerbloreTracker - @chirpchirp#8969'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)


# eh gotta parse through response to get other fields, don't remember how but can figure out
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
abyssalWhip = Item('abyssal whip', 4151, 100, 1, 1, 1)

#once object is created, can access fields from object like this
print(abyssalWhip.highPrice)
