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

    print('Cleaning Herbs Margins')

    for row in reader:
        cleanHerbId = int(row[0])
        grimyHerbId = int(row[1])
        levelReq = int(row[2])

        #print(getItemDetails(cleanHerbId))
        #print(getItemDetails(grimyHerbId))
        print(itemDict[cleanHerbId]['name'].ljust(12) + ': ' + str(itemDict[cleanHerbId]['highPrice']-itemDict[grimyHerbId]['lowPrice']).rjust(3) + ' \tCurrent Prices: ' + getItemDetails(cleanHerbId) + ' ' + getItemDetails(grimyHerbId))
