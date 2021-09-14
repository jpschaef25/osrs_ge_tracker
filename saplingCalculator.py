import requests
import json
import csv
from datetime import datetime
from getItemData import get_all_item_data

def getItemDetails(itemId):
    return itemDict[itemId]['name'] + ' ' + str(itemDict[itemId]['lowPrice']) + '-' + str(itemDict[itemId]['highPrice'])

itemDict = get_all_item_data()

with open('saplings.csv') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        seedId = int(row[0])
        saplingId = int(row[1])
        margin = itemDict[saplingId]['lowPrice'] - itemDict[seedId]['highPrice']
        print (getItemDetails(saplingId) + ' - ' + getItemDetails(seedId) + ' - ' + str(margin))
