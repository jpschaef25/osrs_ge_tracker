import requests
import json
import csv
from datetime import datetime
from getItemData import get_all_item_data

itemDict = get_all_item_data()

# Read potion ingredients from CSV file
with open('herbloreIngredients.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # Cast csv data to int and float
        potionId = int(row[0])
        baseIngId = int(row[1])
        secondaryIngId = int(row[2])
        quantity = int(row[3])
        xp = float(row[4])

        potionSellPrice = itemDict[potionId]['lowPrice']
        ingredientBuyPrice = itemDict[baseIngId]['highPrice'] + (itemDict[secondaryIngId]['highPrice'] * quantity)

        print(row)
        profitPerPot = potionSellPrice - ingredientBuyPrice
        print('Potion Sells For ' + str(potionSellPrice) + ', Ingredients Buy For ' + str(ingredientBuyPrice) + ', Profit Per Potion is ' + str(profitPerPot))
