import requests
import json
import csv
from datetime import datetime
from getItemData import get_all_item_data

def getItemDetails(itemId):
    return itemDict[itemId]['name'] + ' ' + str(itemDict[itemId]['lowPrice']) + '-' + str(itemDict[itemId]['highPrice'])

itemDict = get_all_item_data()

# Find amulet of chemistry price
amuletId = 21163
amuletPrice = itemDict[amuletId]['highPrice']

# Read potion ingredients from CSV file
with open('herbloreIngredients.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # Cast csv data to int and float
        threeDosePotId = int(row[0])
        baseIngId = int(row[1])
        secondaryIngId = int(row[2])
        quantityIngreds = int(row[3])
        xp = float(row[4])
        fourDosePotId = int(row[5])
        dosesMade = int(row[6])
        potsPerHour = int(row[7])
        levelReq = int(row[8])

        # Calculate instant buy/sell without amulet
        potionSellPrice = itemDict[fourDosePotId]['lowPrice'] * (dosesMade/4)
        ingredientBuyPrice = itemDict[baseIngId]['highPrice'] + (itemDict[secondaryIngId]['highPrice'] * quantityIngreds)
        profitPerPot = potionSellPrice - ingredientBuyPrice
        gpPerXpInstant = round(profitPerPot / xp, 2)

        # Calculate patient buy/sell without amulet
        potionSellPrice = itemDict[fourDosePotId]['highPrice'] * (dosesMade/4)
        ingredientBuyPrice = itemDict[baseIngId]['lowPrice'] + (itemDict[secondaryIngId]['lowPrice'] * quantityIngreds)
        profitPerPot = potionSellPrice - ingredientBuyPrice
        gpPerXpPatient = round(profitPerPot / xp, 2)

        # Calculate xp per hour
        xpPerHour = int(xp * potsPerHour)

        # Calculate instant buy/sell with amulet
        if dosesMade == 3:
            potionSellPrice = (0.95 * itemDict[fourDosePotId]['lowPrice'] * (3/4)) + (0.05 * itemDict[fourDosePotId]['lowPrice'])
            ingredientBuyPrice = itemDict[baseIngId]['highPrice'] + (itemDict[secondaryIngId]['highPrice'] * quantityIngreds)
            profitPerPot = potionSellPrice - ingredientBuyPrice - (amuletPrice / 100)
            gpPerXpInstantAmulet = round(profitPerPot / xp, 2)
        else:
            gpPerXpInstantAmulet = 0

        # Calculate patient buy/sell with amulet
        if dosesMade == 3:
            potionSellPrice = (0.95 * itemDict[fourDosePotId]['highPrice'] * (3/4)) + (0.05 * itemDict[fourDosePotId]['highPrice'])
            ingredientBuyPrice = itemDict[baseIngId]['lowPrice'] + (itemDict[secondaryIngId]['lowPrice'] * quantityIngreds)
            profitPerPot = potionSellPrice - ingredientBuyPrice - (amuletPrice / 100)
            gpPerXpPatientAmulet = round(profitPerPot / xp, 2)
        else:
            gpPerXpPatientAmulet = 0

        print(itemDict[fourDosePotId]['name'].ljust(30) + '(' + str(levelReq) + ' required)' + '\tXp/Hr: ' + "{:,}".format(xpPerHour).rjust(7))
        print('GP/XP: w/o Amulet: ' + "{:.2f}".format(gpPerXpInstant).rjust(6) + ' to ' + "{:.2f}".format(gpPerXpPatient).rjust(6) + \
            '\twith Amulet: ' + "{:.2f}".format(gpPerXpInstantAmulet).rjust(6) + ' to ' + "{:.2f}".format(gpPerXpPatientAmulet).rjust(6))

        print('Base: ' + getItemDetails(baseIngId) + ' gp \tSecondary: ' + getItemDetails(secondaryIngId) + ' gp \tPotion: ' + getItemDetails(fourDosePotId) + ' gp')
        print()
