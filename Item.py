class Item:
    name = ''
    highAlch = 0

    def __init__(self, itemId, highPrice, highTime, lowPrice, lowTime):
        self.itemId = itemId
        self.highPrice = highPrice
        self.highTime = highTime
        self.lowPrice = lowPrice
        self.lowTime = lowTime

    def __str__(self):
        return str('ItemID=' + str(self.itemId) + \
            ', HighPrice=' + str(self.highPrice) + \
            ', HighTime=' + str(self.highTime.strftime("%m/%d/%Y, %H:%M:%S")) + \
            ', LowPrice=' + str(self.lowPrice) + \
            ', LowTime=' + str(self.lowTime.strftime("%m/%d/%Y, %H:%M:%S")) + \
            ', Name=' + str(self.name) + \
            ', HighAlch=' + str(self.highAlch))
