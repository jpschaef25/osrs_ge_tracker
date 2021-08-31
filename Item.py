class Item:

    def __init__(self, name, id, highPrice, highTime, lowPrice, lowTime):
        self.name = name
        self.id = id
        self.highPrice = highPrice
        self.highTime = highTime
        self.lowPrice = lowPrice
        self.lowTime = lowTime


    def __str__(self):
        return str(self.id) \
               + '::' + self.name \
               + '::' + self.highPrice \
               + '::' + self.highTime \
               + '::' + self.lowPrice \
               + '::' + self.lowTime
