import requests
import json
import csv
from datetime import datetime
from Item import Item

# Setup headers for API call so they can yell at me if we use API too heavily
headers = {
    'User-Agent': 'TestHerbloreTracker - @chirpchirp#8969'
}

# Call API to get latest GE prices
url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
response = requests.get(url, headers=headers)
itemList = response.json()

# itemDict will contain the following fields: highPrice, highTime, lowPrice, lowTime, name, HighAlch
# Access fields by itemId like this: "itemDict[itemId]['name']""
itemDict = {}

# Adds highPrice, highTime, lowPrice, lowTime to itemDict
for item in itemList['data'].items():
    # Ignores any items that haven't been traded on GE
    if item[1]['highTime'] is None or item[1]['lowTime'] is None:
        print('Fake item')
    else:
        itemId = int(item[0])
        itemDict[itemId] = {}
        itemDict[itemId]['highPrice'] = item[1]['high']
        itemDict[itemId]['highTime'] = datetime.fromtimestamp(item[1]['highTime'])
        itemDict[itemId]['lowPrice'] = item[1]['low']
        itemDict[itemId]['lowTime'] = datetime.fromtimestamp(item[1]['lowTime'])

# Call API to get item ID, name, high alch mappings
mapping_url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
response2 = requests.get(mapping_url, headers=headers)
mappingList = response2.json()

# Adds item name and high alch value to itemDict
for mapping in mappingList:
    itemId = int(mapping['id'])
    # POTENTIAL ISSUE: Some ingredients may not trade on GE so they might not already be in itemDict
    # Need to figure out a way to get values for these (i.e. amylase crystals) ... or ignore them
    if itemId in itemDict:
        itemDict[itemId]['name'] = mapping['name']
        if 'highalch' in mapping:
            itemDict[itemId]['highAlch'] = mapping['highalch']

print('Item Dictionary Created')

# Read potion ingredients from CSV file
with open('herbloreIngredients.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


def get_highPrice(itemID):
    print('This should iterate through the list and grab the highPrice for the given itemID')
    return itemDict[itemId]['highPrice']

def get_lowPrice(itemID):
    print('This should iterate through the list and grab the lowPrice for the given itemID')
    return itemDict[itemId]['lowPrice']
