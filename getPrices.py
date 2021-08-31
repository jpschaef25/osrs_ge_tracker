import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
from Item import Item

url = 'https://prices.runescape.wiki/api/v1/osrs/latest'

headers = {
    'User-Agent': 'TestHerbloreTracker - @chirpchirp#8969'
}

response = requests.get(url, headers=headers)

itemList = response.json()

allItems= []

for item in itemList['data'].items():

    if item[1]['highTime'] is None or item[1]['lowTime'] is None:
        print('Fake item')
    else:
        itemId = item[0]
        highPrice = item[1]['high']
        highTime = datetime.fromtimestamp(item[1]['highTime'])
        lowPrice = item[1]['low']
        lowTime = datetime.fromtimestamp(item[1]['lowTime'])
        # print('ItemID=' + str(itemId) + ', HighPrice=' + str(highPrice) + ', HighTime=' + str(highTime.strftime("%m/%d/%Y, %H:%M:%S")) + ', LowPrice=' + str(lowPrice) + ', LowTime=' + str(lowTime.strftime("%m/%d/%Y, %H:%M:%S")))

        myItem = Item(itemId, highPrice, highTime, lowPrice, lowTime)

        allItems.append(myItem)

        #print(str(myItem))

mapping_url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'

response2 = requests.get(mapping_url, headers=headers)

mappingList = response2.json()

for mapping in mappingList:
    for item in allItems:
        if int(mapping['id']) == int(item.itemId):
            item.name = mapping['name']
            if mapping.has_key('highalch'):
                item.highAlch = mapping['highalch']
            print(str(item))

print('end')

# for key, value in itemList['data']:
    # print(key + ' : HighPrice=' + value['high'])


def get_highPrice(itemID):
    print('This should iterate through the list and grab the highPrice for the given itemID')

def get_lowPrice(itemID):
    print('This should iterate through the list and grab the lowPrice for the given itemID')


# eh gotta parse through response to get other fields, don't remember how but can figure out
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#abyssalWhip = Item('abyssal whip', 4151, 100, 1, 1, 1)

#once object is created, can access fields from object like this
#print(abyssalWhip.highPrice)
