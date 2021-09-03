import requests
import json
import csv
from datetime import datetime
from getItemData import get_all_item_data

def getItemDetails(itemId):
    return itemDict[itemId]['name'] + ' ' + str(itemDict[itemId]['lowPrice']) + '-' + str(itemDict[itemId]['highPrice'])

itemDict = get_all_item_data()

with open('herbs.csv') as f:
    reader = csv.reader(f)
    next(reader)

    print('Cleaning Herbs Calculator')

    for row in reader:
        cleanHerbId = int(row[0])
        grimyHerbId = int(row[1])
        levelReq = int(row[2])

        #print(getItemDetails(cleanHerbId))
        #print(getItemDetails(grimyHerbId))
        print(itemDict[cleanHerbId]['name'].ljust(12) + ': ' + str(itemDict[cleanHerbId]['lowPrice']-itemDict[grimyHerbId]['highPrice']).rjust(3) + ' \tCurrent Prices: ' + getItemDetails(cleanHerbId) + ', ' + getItemDetails(grimyHerbId))

with open('herbs.csv') as f:
    reader = csv.reader(f)
    next(reader)

    print()
    print('Unfinished Potions Calculator')

    for row in reader:
        cleanHerbId = int(row[0])
        unfPotionId = int(row[3])

        print(itemDict[unfPotionId]['name'].ljust(30) + ': ' + str(itemDict[unfPotionId]['lowPrice']-itemDict[cleanHerbId]['highPrice']).rjust(3) + ' \tCurrent Prices: ' + getItemDetails(unfPotionId) + ', ' + getItemDetails(cleanHerbId))
