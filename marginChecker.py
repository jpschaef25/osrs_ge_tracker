import requests
import json
import csv
from datetime import datetime
from getItemData import get_all_item_data

def getItemDetails(itemId):
    return itemDict[itemId]['name'] + ' ' + str(itemDict[itemId]['lowPrice']) + '-' + str(itemDict[itemId]['highPrice'])

itemDict = get_all_item_data()

with open('marginItems.csv') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        print (getItemDetails(int(row[0])))
